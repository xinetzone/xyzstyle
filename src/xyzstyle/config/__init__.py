"""配置管理模块，提供 Sphinx 文档主题配置的加载、验证和管理功能。

此模块是 XYZStyle 主题的配置管理入口点，负责导出核心配置管理类
供主题系统使用。

导出:
    ConfigManager: 配置管理的核心类，负责加载、验证和应用 TOML 配置文件。
"""
from .manager import ConfigManager


__all__ = ['ConfigManager']