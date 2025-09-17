from dataclasses import dataclass, field
import tomllib
from pathlib import Path
from typing import Any, Dict, Optional, cast
from sphinx.application import Sphinx
from sphinx.util import logging
from sphinx.config import Config

# 获取Sphinx日志记录器
logger = logging.getLogger(__name__)

class ConfigManager:
    """配置管理器，负责处理主题相关的配置加载和应用。
    
    该类提供了从TOML文件加载配置、合并默认配置与用户配置
    以及应用配置到Sphinx实例的功能。
    """
    
    def __init__(self, app: Sphinx, config: Config) -> None:
        """初始化配置管理器。
        
        Args:
            app: Sphinx应用实例
            config: Sphinx配置对象
        """
        self.app = app
        self.config = config
        self.logger = logging.getLogger(f"{__name__}.ConfigManager")
        
    def load_default_config(self) -> Optional[Dict[str, Any]]:
        """加载默认配置文件。
        
        Returns:
            配置字典，如果文件不存在则返回None
        """
        default_toml = Path(self.app.srcdir) / "default.toml"
        if not default_toml.exists():
            self.logger.warning(f"未找到默认配置文件 {default_toml}，跳过配置更新")
            return None
        
        try:
            with open(default_toml, "rb") as f:
                default_config = tomllib.load(f)
                self.logger.info(f"成功加载默认配置文件 {default_toml}")
                return default_config
        except Exception as e:
            self.logger.error(f"加载默认配置文件时出错: {e}")
            raise
    
    def apply_config(self) -> None:
        """应用加载的配置到Sphinx配置对象。
        
        主要处理html_theme_options的合并。
        """
        default_config = self.load_default_config()
        if not default_config:
            return
        
        if "html_theme_options" in default_config:
            if not hasattr(self.config, "html_theme_options"):
                self.config.html_theme_options = {}
            
            # 合并默认配置到html_theme_options
            for key, value in default_config["html_theme_options"].items():
                if key not in self.config.html_theme_options:
                    self.config.html_theme_options[key] = value
                    self.logger.debug(f"应用默认配置: {key} = {value}")
            
            self.logger.info(f"已成功更新html_theme_options配置")


def config_inited_handler(app: Sphinx, config: Config) -> None:
    """config-inited 事件处理器
    
    在 Sphinx 完成配置对象（Config）初始化后立即触发，让你有机会在构建器（Builder）创建之前，读取或修改配置。
    
    触发时机
        - 发生在：conf.py 执行完毕，所有配置变量已收集并封装到 Config 对象中。
        - 早于：builder-inited（构建器初始化）事件。
        - 晚于：扩展加载（extensions 列表中的扩展已导入）。
            - 因为 extensions 已经加载完毕，所以在 config-inited 中修改 extensions 列表不会重新加载扩展。
              如果需要动态加载扩展，应使用 app.setup_extension()。
    
    Args:
        app: Sphinx应用实例
        config: Sphinx配置对象
    """
    logger.info("初始化mystx配置系统")
    try:
        config_manager = ConfigManager(app=app, config=config)
        config_manager.apply_config()
    except Exception as e:
        logger.error(f"配置系统初始化失败: {e}")
        raise


@dataclass
class MySTX:
    """mystx主题管理类，负责整合主题信息管理和配置功能。
    
    该类负责查找主题目录、注册主题到Sphinx应用，并设置配置加载器事件处理函数。
    
    Attributes:
        app: Sphinx应用实例，用于注册主题和连接事件。
        name: 主题名称，默认为"mystx"。
        theme_dir: 主题目录路径，初始化后自动设置。
    """
    app: Sphinx
    name: str = "mystx"
    theme_dir: Optional[str] = field(init=False)
    
    def __post_init__(self) -> None:
        """初始化后处理函数，查找主题目录并注册主题。
        
        此方法在类实例化后自动调用，负责确定主题目录的绝对路径，
        验证目录存在性，然后将主题注册到Sphinx应用并连接配置初始化事件。
        
        Raises:
            FileNotFoundError: 如果主题目录不存在。
        """
        # 确定主题目录的绝对路径
        parent = Path(__file__).parent.resolve()
        theme_dir = parent / "theme" / self.name
        
        # 验证主题目录是否存在
        if not theme_dir.exists():
            logger.error(f"主题目录未找到: {theme_dir}")
            raise FileNotFoundError(f"主题目录未找到: {theme_dir}")
        
        self.theme_dir = str(theme_dir)
        try:
            # 注册主题到Sphinx应用
            self.app.add_html_theme(self.name, self.theme_dir)
            # 连接到配置初始化事件
            self.app.connect('config-inited', config_inited_handler)
        except Exception as e:
            logger.error(f"注册 {self.name} 主题时发生错误: {e}")
            raise
        
        logger.info(f"{self.name} 主题已成功注册")
