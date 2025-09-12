"""xyzstyle - A Sphinx theme for documentation.

This module provides a custom Sphinx theme for creating beautiful documentation.
"""

import tomllib
from pathlib import Path
from typing import Any, Dict

from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata
from sphinx.util import logging
from .config_loader import load_toml_config

# 获取Sphinx日志记录器
logger = logging.getLogger(__name__)


def get_html_theme_path() -> str:
    """Return the path to the HTML theme directory.

    Returns:
        str: Absolute path to the theme directory.
    """
    parent = Path(__file__).parent.resolve()
    return f"{parent}/theme/xyzstyle"

def load_toml_config_event(app: Sphinx, config: Dict[str, Any]) -> None:
    """在 Sphinx 配置初始化后加载 TOML 配置。

    Args:
        app: Sphinx 应用实例
        config: Sphinx 配置对象
    """
    try:
        # 获取文档源目录的绝对路径
        src_dir = Path(app.srcdir)
        config_path = src_dir / "doc.toml"
        logger.debug(f"Attempting to load TOML configuration from {config_path}")
        
        # 尝试加载 doc.toml 配置
        toml_config = load_toml_config(str(config_path))
        logger.info(f"Successfully loaded TOML configuration from {config_path}")
        
        # 更新 Sphinx 配置对象
        updated_count = 0
        for key, value in toml_config.items():
            if hasattr(config, key):
                old_value = getattr(config, key)
                setattr(config, key, value)
                logger.debug(f"Updated configuration '{key}': {old_value} -> {value}")
                updated_count += 1
        
        if updated_count > 0:
            logger.info(f"Updated {updated_count} configuration settings from TOML file")
        else:
            logger.debug("No configuration settings were updated from the TOML file")
            
    except FileNotFoundError as e:
        # 配置文件不存在是可预期的常见情况，使用较低的警告级别
        logger.warning(f"TOML configuration file not found: {e}")
        logger.info("Using default configuration from conf.py")
        # 当配置文件不存在时，不进行任何操作，让 Sphinx 使用 conf.py 中的默认配置
    except Exception as e:
        # 其他未预期的错误
        logger.error(f"Unexpected error loading TOML configuration: {e}")
        logger.info("Falling back to default configuration from conf.py")

def setup(app: Sphinx) -> ExtensionMetadata:
    """Set up the xyzstyle Sphinx theme.

    This function is called by Sphinx when the extension is loaded.

    Args:
        app: Sphinx application instance.

    Returns:
        ExtensionMetadata: Dictionary of metadata for the extension.
    """
    theme_dir = get_html_theme_path()
    app.add_html_theme("xyzstyle", theme_dir)
    
    # 连接到 config-inited 事件，在配置初始化后加载 TOML 配置
    app.connect('config-inited', load_toml_config_event)
    
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
