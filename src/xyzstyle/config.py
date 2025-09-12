import tomllib
from pathlib import Path
from sphinx.util import logging
from typing import Dict, Any, Optional, Union, List, Type, get_type_hints
from dataclasses import dataclass, field, InitVar

# 获取Sphinx日志记录器
logger = logging.getLogger(__name__)

class ConfigValidationError(Exception):
    """配置验证错误的自定义异常类"""

@dataclass
class SphinxConfig:
    """Sphinx配置的完整数据结构"""
    project: str = "Unknown Project"
    author: str = "Unknown Author"
    version: str = "0.0.1"
    release: str = "0.0.1"
    copyright: str = ""
    language: str = "en"
    exclude_patterns: List[str] = field(default_factory=list)
    html_theme: str = "xyzstyle"
    html_title: Optional[str] = ""
    html_static_path: List[str] = field(default_factory=lambda: ["_static"])
    html_favicon: Optional[str] = None
    html_logo: Optional[str] = None
    html_theme_options: Dict[str, Any] = field(default_factory=dict)
    extensions: List[str] = field(default_factory=list)

@dataclass
class ConfigManager:
    """配置管理器，整合了配置加载和更新功能"""
    # 用于配置更新的参数
    app: Optional['Sphinx'] = None
    config: Optional[Dict[str, Any]] = None
    updated_count: int = 0
    config_path: Optional[Path] = None
    
    # 用于配置加载的内部状态
    _data: Dict[str, Any] = field(init=False, default_factory=dict)
    _direct_path: Optional[InitVar[str]] = None
    
    def __post_init__(self, _direct_path: Optional[str] = None):
        """初始化后处理配置加载和更新"""
        # 如果提供了直接路径，则只加载配置而不更新
        if _direct_path:
            self._load_toml_file(_direct_path)
            return
        
        # 如果提供了app和config，则进行完整的配置加载和更新
        if self.app is None or self.config is None:
            logger.error("无法更新配置：缺少应用实例或配置对象")
            return
        
        try:
            # 获取文档源目录的绝对路径并设置配置文件路径
            self._set_config_path()
            
            # 加载并验证TOML配置
            toml_config = self._load_toml_config()
            
            # 更新 Sphinx 配置
            self._update_sphinx_config(toml_config)
                
        except FileNotFoundError as e:
            # 配置文件不存在是可预期的常见情况
            logger.warning(f"未找到 TOML 配置文件: {e}")
            logger.info("将使用 conf.py 中的默认配置")
        except (ConfigValidationError, Exception) as e:
            # 处理配置验证错误和其他异常
            error_type = "配置验证失败" if isinstance(e, ConfigValidationError) else "发生未预期的错误"
            logger.error(f"加载 TOML 配置时{error_type}: {e}")
            logger.info("将使用 conf.py 中的默认配置")
    
    def validate(self, value: Any, expected_type: type, field_name: str) -> None:
        """验证配置值的类型"""
        # 如果值为None且字段是可选的，则通过验证
        if value is None and self._is_optional_type(expected_type):
            return
        
        # 处理泛型类型
        if hasattr(expected_type, "__origin__"):
            # 处理列表类型
            if expected_type.__origin__ in (list, List):
                if not isinstance(value, list):
                    raise ConfigValidationError(f"配置项 '{field_name}' 应为列表类型，实际为: {type(value).__name__}")
            # 处理字典类型
            elif expected_type.__origin__ in (dict, Dict):
                if not isinstance(value, dict):
                    raise ConfigValidationError(f"配置项 '{field_name}' 应为字典类型，实际为: {type(value).__name__}")
            # 处理联合类型
            elif expected_type.__origin__ == Union:
                # 检查值是否匹配联合类型中的任何一个
                if not any(isinstance(value, t) for t in expected_type.__args__ if t is not type(None)):
                    type_names = [t.__name__ for t in expected_type.__args__ if t is not type(None)]
                    if type(None) in expected_type.__args__:
                        type_names.append("None")
                    raise ConfigValidationError(f"配置项 '{field_name}' 类型应为以下之一: {', '.join(type_names)}，实际为: {type(value).__name__}")
        # 普通类型验证
        else:
            try:
                if not isinstance(value, expected_type):
                    raise ConfigValidationError(f"配置项 '{field_name}' 类型应为 {expected_type.__name__}，实际为: {type(value).__name__}")
            except TypeError:
                # 处理无法直接用于isinstance检查的类型
                pass
    
    def _is_optional_type(self, expected_type: type) -> bool:
        """检查类型是否为Optional[T]"""
        # 检查是否是Union[T, None]类型
        if hasattr(expected_type, "__origin__") and expected_type.__origin__ == Union and type(None) in expected_type.__args__:
            return True
        # 检查是否是直接使用Optional的情况
        if str(expected_type).startswith("typing.Optional"):
            return True
        return False
    
    def _load_toml_file(self, config_path: str) -> None:
        """加载并解析TOML配置文件"""
        path = Path(config_path)
        logger.debug(f"尝试从 {path} 加载 TOML 配置")
        
        if not path.exists():
            logger.error(f"TOML 配置文件不存在: {config_path}")
            raise FileNotFoundError(f"TOML 配置文件不存在: {config_path}")

        try:
            with path.open("rb") as f:
                self._data = tomllib.load(f)
            
            logger.debug(f"成功解析 TOML 配置文件: {path}")
        except tomllib.TOMLDecodeError as e:
            logger.error(f"TOML 配置文件格式错误: {e}")
            raise ConfigValidationError(f"TOML 配置文件格式错误: {e}")
        except PermissionError:
            logger.error(f"没有权限读取配置文件: {path}")
            raise PermissionError(f"没有权限读取配置文件: {path}")
        except Exception as e:
            logger.error(f"读取配置文件时发生未知错误: {e}")
            raise
    
    @property
    def config_dict(self) -> Dict[str, Any]:
        """获取Sphinx可用的配置字典"""
        # 获取默认配置值
        default_config = SphinxConfig()
        
        # 从TOML数据中提取配置值
        project_data = self._data.get("project", {})
        html_data = self._data.get("html", {})
        
        # 构建配置字典，直接应用映射
        config = {
            "project": project_data.get("name", default_config.project),
            "author": project_data.get("author", default_config.author),
            "version": project_data.get("version", default_config.version),
            "release": project_data.get("version", default_config.release),
            "copyright": project_data.get("copyright", default_config.copyright),
            "language": self._data.get("language", default_config.language),
            "exclude_patterns": self._data.get("exclude_patterns", default_config.exclude_patterns),
            "html_theme": html_data.get("theme", default_config.html_theme),
            "html_title": html_data.get("title", default_config.html_title),
            "html_static_path": html_data.get("static_path", default_config.html_static_path),
            "html_favicon": html_data.get("favicon", default_config.html_favicon),
            "html_logo": html_data.get("logo", default_config.html_logo),
            "html_theme_options": html_data.get("theme_options", default_config.html_theme_options),
            "extensions": self._data.get("extensions", default_config.extensions)
        }
        
        # 验证配置类型
        self._validate_config(config)
        
        logger.debug(f"将 TOML 配置映射到 Sphinx 设置: {list(config.keys())}")
        return config
        
    def _validate_config(self, config: Dict[str, Any]) -> None:
        """统一验证配置对象的类型"""
        type_hints = get_type_hints(SphinxConfig)
        
        for key, value in config.items():
            if key in type_hints:
                try:
                    # 对所有字段进行统一验证，包括主题选项和扩展
                    self.validate(value, type_hints[key], key)
                except ConfigValidationError as e:
                    logger.error(f"配置验证失败: {e}")
                    raise
            else:
                logger.warning(f"未在SphinxConfig中定义的配置项: {key}")
    
    def _set_config_path(self) -> None:
        """设置配置文件路径"""
        src_dir = Path(self.app.srcdir)
        self.config_path = src_dir / "doc.toml"
    
    def _load_toml_config(self) -> Dict[str, Any]:
        """加载并验证TOML配置"""
        logger.debug(f"尝试加载 TOML 配置文件: {self.config_path}")
        # 使用内部方法直接加载，避免创建新的ConfigManager实例
        self._load_toml_file(str(self.config_path))
        toml_config = self.config_dict
        logger.info(f"成功加载 TOML 配置文件: {self.config_path}")
        return toml_config
    
    def _update_sphinx_config(self, toml_config: Dict[str, Any]) -> None:
        """更新 Sphinx 配置"""
        self.updated_count = 0
        for key, value in toml_config.items():
            if hasattr(self.config, key):
                old_value = getattr(self.config, key)
                setattr(self.config, key, value)
                logger.debug(f"更新配置项 '{key}': {old_value} -> {value}")
                self.updated_count += 1
            else:
                logger.warning(f"未知的配置项 '{key}' 将被忽略")
        
        if self.updated_count > 0:
            logger.info(f"从 TOML 文件更新了 {self.updated_count} 个配置设置")

