import tomllib
from pathlib import Path
from sphinx.util import logging
from typing import Dict, Any, Optional, Union, List, Type, get_type_hints, Callable, Final
from dataclasses import dataclass, field, InitVar

# 获取Sphinx日志记录器
logger = logging.getLogger(__name__)

class ConfigValidationError(Exception):
    """配置验证错误的自定义异常类。
    
    当TOML配置文件中的值类型不符合预期或格式不正确时抛出此异常。
    """

@dataclass
class SphinxConfig:
    """Sphinx配置的完整数据结构。
    
    这个数据类定义了Sphinx文档项目的主要配置项及其默认值。
    它用于配置验证和作为配置加载的参考结构。
    """
    # 项目基本信息
    project: str = "Unknown Project"  # 项目名称
    author: str = "Unknown Author"  # 项目作者
    version: str = "0.0.1"  # 项目版本号(主版本.次版本)
    release: str = "0.0.1"  # 项目发布号(完整版本号)
    copyright: str = ""  # 版权声明
    language: str = "en"  # 文档语言
    
    # 构建配置
    exclude_patterns: List[str] = field(default_factory=list)  # 构建时排除的文件模式列表
    
    # HTML输出配置
    html_theme: str = "xyzstyle"  # HTML主题名称
    html_title: Optional[str] = ""  # HTML页面标题
    html_static_path: List[str] = field(default_factory=lambda: ["_static"])  # 静态文件目录列表
    html_favicon: Optional[str] = None  # 网站图标路径
    html_logo: Optional[str] = None  # 网站Logo路径
    html_theme_options: Dict[str, Any] = field(default_factory=dict)  # 主题特定选项
    
    # 扩展配置
    extensions: List[str] = field(default_factory=list)  # 启用的Sphinx扩展列表

@dataclass
class ConfigManager:
    """配置管理器，整合了配置加载和更新功能。
    
    这个类负责从TOML文件加载配置，并将配置应用到Sphinx应用实例中。
    它支持配置验证、类型检查和增量更新。
    """
    # 用于配置更新的参数
    app: Optional['Sphinx'] = None  # Sphinx应用实例
    config: Optional[Dict[str, Any]] = None  # Sphinx配置对象
    updated_count: int = 0  # 更新的配置项数量计数器
    config_path: Optional[Path] = None  # 配置文件路径
    
    # 用于配置加载的内部状态
    _data: Dict[str, Any] = field(init=False, default_factory=dict)  # 从TOML文件加载的原始数据
    _direct_path: Optional[InitVar[str]] = None  # 直接加载配置文件的路径（初始化变量）
    
    # 配置映射常量：将TOML配置映射到Sphinx配置
    _CONFIG_MAPPING: Final[Dict[str, tuple[str, str, str]]] = field(
        init=False,
        default_factory=lambda: {
            "project": ("project", "name", "project"),  # (TOML节, TOML键, Sphinx属性)
            "author": ("project", "author", "author"),
            "version": ("project", "version", "version"),
            "release": ("project", "version", "release"),
            "copyright": ("project", "copyright", "copyright"),
            "language": ("", "language", "language"),
            "exclude_patterns": ("", "exclude_patterns", "exclude_patterns"),
            "html_theme": ("html", "theme", "html_theme"),
            "html_title": ("html", "title", "html_title"),
            "html_static_path": ("html", "static_path", "html_static_path"),
            "html_favicon": ("html", "favicon", "html_favicon"),
            "html_logo": ("html", "logo", "html_logo"),
            "html_theme_options": ("html", "theme_options", "html_theme_options"),
            "extensions": ("", "extensions", "extensions")
        }
    )
    
    def __post_init__(self, _direct_path: Optional[str] = None) -> None:
        """初始化后处理配置加载和更新。
        
        根据初始化参数，该方法执行以下操作之一：
        1. 如果提供了_direct_path，仅加载指定路径的TOML配置。
        2. 如果提供了app和config，加载配置并更新Sphinx应用的配置。
        3. 如果缺少必要参数，记录错误并退出。
        
        Args:
            _direct_path: 可选的直接配置文件路径，用于仅加载配置而不更新。
            
        Raises:
            FileNotFoundError: 如果配置文件不存在（但会被内部捕获并记录警告）。
            ConfigValidationError: 如果配置验证失败（但会被内部捕获并记录错误）。
            Exception: 如果发生其他未预期的错误（但会被内部捕获并记录错误）。
        """
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
        """验证配置值的类型是否符合预期。
        
        此方法支持验证基本类型、泛型类型（如List、Dict）和联合类型（如Union、Optional）。
        
        Args:
            value: 要验证的配置值。
            expected_type: 预期的类型。
            field_name: 配置字段名称，用于错误消息。
            
        Raises:
            ConfigValidationError: 如果值的类型不符合预期。
        """
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
        """检查类型是否为Optional[T]（即可为None的类型）。
        
        Args:
            expected_type: 要检查的类型。
            
        Returns:
            bool: 如果类型是Optional[T]，返回True；否则返回False。
        """
        # 检查是否是Union[T, None]类型
        if hasattr(expected_type, "__origin__") and expected_type.__origin__ == Union and type(None) in expected_type.__args__:
            return True
        # 检查是否是直接使用Optional的情况
        if str(expected_type).startswith("typing.Optional"):
            return True
        return False
    
    def _load_toml_file(self, config_path: str) -> None:
        """加载并解析TOML配置文件。
        
        此方法负责打开指定路径的TOML文件，解析其内容，并将结果存储在内部_data属性中。
        
        Args:
            config_path: TOML配置文件的路径。
            
        Raises:
            FileNotFoundError: 如果配置文件不存在。
            ConfigValidationError: 如果TOML文件格式错误。
            PermissionError: 如果没有权限读取配置文件。
            Exception: 如果发生其他未知错误。
        """
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
        """获取Sphinx可用的配置字典。
        
        此属性方法使用预定义的配置映射将TOML配置数据转换为Sphinx可用的配置字典。
        它处理默认值、节数据提取和特殊情况处理，并在返回前验证配置类型。
        
        Returns:
            Dict[str, Any]: 包含Sphinx配置键值对的字典。
            
        Raises:
            ConfigValidationError: 如果配置验证失败。
        """
        # 获取默认配置值
        default_config = SphinxConfig()
        config = {}
        
        # 使用配置映射构建配置字典，提高可维护性
        for sphinx_key, (section, toml_key, default_attr) in self._CONFIG_MAPPING.items():
            # 获取默认值
            default_value = getattr(default_config, default_attr)
            
            # 根据section获取相应的数据
            if section == "project":
                source_data = self._data.get("project", {})
            elif section == "html":
                source_data = self._data.get("html", {})
            else:
                source_data = self._data
            
            # 获取配置值，设置默认值
            config[sphinx_key] = source_data.get(toml_key, default_value)
            
            # 特殊处理：release使用与version相同的值
            if sphinx_key == "release" and section == "project" and toml_key == "version":
                config[sphinx_key] = source_data.get(toml_key, default_value)
        
        # 验证配置类型
        self._validate_config(config)
        
        logger.debug(f"将 TOML 配置映射到 Sphinx 设置: {list(config.keys())}")
        return config
        
    def _validate_config(self, config: Dict[str, Any]) -> None:
        """统一验证配置对象的类型。
        
        此方法使用SphinxConfig类的类型提示来验证配置字典中的每个值的类型。
        它会记录警告或在验证失败时抛出异常。
        
        Args:
            config: 包含配置键值对的字典。
            
        Raises:
            ConfigValidationError: 如果任何配置项的类型验证失败。
        """
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
        """设置配置文件路径。
        
        此方法基于Sphinx应用的源码目录确定doc.toml配置文件的路径。
        """
        src_dir = Path(self.app.srcdir)
        self.config_path = src_dir / "doc.toml"
    
    def _load_toml_config(self) -> Dict[str, Any]:
        """加载并验证TOML配置。
        
        此方法加载配置文件，解析其内容，并将其转换为验证过的Sphinx配置字典。
        
        Returns:
            Dict[str, Any]: 验证过的Sphinx配置字典。
            
        Raises:
            FileNotFoundError: 如果配置文件不存在。
            ConfigValidationError: 如果配置验证失败。
        """
        logger.debug(f"尝试加载 TOML 配置文件: {self.config_path}")
        # 使用内部方法直接加载，避免创建新的ConfigManager实例
        self._load_toml_file(str(self.config_path))
        toml_config = self.config_dict
        logger.info(f"成功加载 TOML 配置文件: {self.config_path}")
        return toml_config
    
    def _update_sphinx_config(self, toml_config: Dict[str, Any]) -> None:
        """更新Sphinx配置。
        
        此方法将验证过的TOML配置应用到Sphinx配置对象。
        它执行增量更新，仅当值发生变化时才更新，并记录详细的更新统计信息。
        
        Args:
            toml_config: 包含Sphinx配置键值对的字典。
        """
        if self.config is None:
            logger.error("无法更新配置：配置对象为空")
            return
            
        self.updated_count = 0
        updated_keys = []
        skipped_keys = []
        
        # 批量更新配置
        for key, value in toml_config.items():
            if hasattr(self.config, key):
                old_value = getattr(self.config, key)
                # 仅当值发生变化时更新并记录
                if old_value != value:
                    setattr(self.config, key, value)
                    logger.debug(f"更新配置项 '{key}': {old_value} -> {value}")
                    self.updated_count += 1
                    updated_keys.append(key)
            else:
                logger.warning(f"未知的配置项 '{key}' 将被忽略")
                skipped_keys.append(key)
        
        # 记录更新统计信息
        if self.updated_count > 0:
            logger.info(f"从 TOML 文件更新了 {self.updated_count} 个配置设置: {', '.join(updated_keys)}")
        if skipped_keys:
            logger.debug(f"跳过了 {len(skipped_keys)} 个未知配置项")
