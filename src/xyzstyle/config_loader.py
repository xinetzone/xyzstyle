import tomllib
from pathlib import Path
from sphinx.util import logging

# 获取Sphinx日志记录器
logger = logging.getLogger(__name__)

def load_toml_config(path: str) -> dict:
    """读取 TOML 配置并转换为 Sphinx 可用的字典"""
    config_path = Path(path)
    logger.debug(f"Attempting to load TOML configuration from {config_path}")
    
    if not config_path.exists():
        raise FileNotFoundError(f"TOML 配置文件不存在: {path}")

    with config_path.open("rb") as f:
        data = tomllib.load(f)
    
    logger.debug("Successfully parsed TOML configuration file")

    # 映射 TOML 到 Sphinx 配置 - 不包含extensions配置，避免语义冗余
    # xyzstyle扩展应该在conf.py中声明，而不是在doc.toml中重复定义
    sphinx_conf = {
        "project": data.get("project", {}).get("name", "Unknown Project"),
        "author": data.get("project", {}).get("author", "Unknown Author"),
        "version": data.get("project", {}).get("version", "0.0.1"),
        "release": data.get("project", {}).get("version", "0.0.1"),
        "html_theme": data.get("html", {}).get("theme", "xyzstyle"),
        "html_static_path": data.get("html", {}).get("static_path", ["_static"]),
    }
    
    logger.debug(f"Mapped TOML configuration to Sphinx settings: {list(sphinx_conf.keys())}")
    return sphinx_conf
