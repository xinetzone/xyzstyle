from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Optional
from dataclasses import dataclass, field
from sphinx.application import Sphinx
from sphinx.util import logging
from .config import ConfigManager

# 获取Sphinx日志记录器
logger = logging.getLogger(__name__)

@dataclass
class XYZStyleTheme:
    """XYZStyle主题管理类，整合了主题信息管理和配置功能"""
    app: Sphinx
    name: str = "xyzstyle"
    theme_dir: Optional[str] = field(init=False)
    
    def __post_init__(self) -> None:
        parent = Path(__file__).parent.resolve()
        theme_dir = parent / "theme" / self.name
        if not theme_dir.exists():
            logger.error(f"主题目录未找到: {theme_dir}")
            raise FileNotFoundError(f"主题目录未找到: {theme_dir}")
        self.theme_dir = theme_dir
        try:
            # 注册主题
            self.app.add_html_theme(self.name, self.theme_dir)
            # 连接到配置初始化事件
            self.app.connect('config-inited', self._create_config_loader_event())
            logger.info(f"{self.name} 主题已成功注册")
        except Exception as e:
            logger.error(f"注册 {self.name} 主题时发生错误: {e}")
    
    def _create_config_loader_event(self):
        """创建配置加载器事件处理函数"""
        # 使用lambda表达式简化代码结构
        return lambda app, config: ConfigManager(app=app, config=config)
