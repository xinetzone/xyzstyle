from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, Optional
from sphinx.application import Sphinx
from sphinx.util import logging
from .config import ConfigManager

# 获取Sphinx日志记录器
logger = logging.getLogger(__name__)

@dataclass
class XYZStyleTheme:
    """XYZStyle主题管理类，负责整合主题信息管理和配置功能。
    
    该类负责查找主题目录、注册主题到Sphinx应用，并设置配置加载器事件处理函数。
    
    Attributes:
        app: Sphinx应用实例，用于注册主题和连接事件。
        name: 主题名称，默认为"xyzstyle"。
        theme_dir: 主题目录路径，初始化后自动设置。
    """
    app: Sphinx
    name: str = "xyzstyle"
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
        
        self.theme_dir = theme_dir
        try:
            # 注册主题到Sphinx应用
            self.app.add_html_theme(self.name, self.theme_dir)
            # 连接到配置初始化事件
            self.app.connect('config-inited', self._create_config_loader_event())
            logger.info(f"{self.name} 主题已成功注册")
        except Exception as e:
            logger.error(f"注册 {self.name} 主题时发生错误: {e}")
    
    def _create_config_loader_event(self) -> Callable[[Sphinx, Dict[str, Any]], ConfigManager]:
        """创建配置加载器事件处理函数。
        
        返回一个lambda函数，该函数在配置初始化事件触发时被调用，
        用于创建ConfigManager实例以加载和应用TOML配置。
        
        Returns:
            Callable: 接受Sphinx应用和配置对象作为参数的事件处理函数。
        """
        # 使用lambda表达式创建配置管理器实例
        return lambda app, config: ConfigManager(app=app, config=config)
