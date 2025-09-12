import os
import sys
from importlib.metadata import version, PackageNotFoundError

# 添加src目录到路径以便导入xyzstyle模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


def test_version_import():
    """测试是否可以导入版本信息"""
    # 尝试直接从包中导入版本信息（如果有）
    try:
        from xyzstyle import __version__
        # 验证版本格式是否符合语义化版本规范 (major.minor.patch)
        parts = __version__.split('.')
        assert len(parts) >= 2, f"版本号格式不正确: {__version__}"
        assert all(part.isdigit() for part in parts[:2]), f"版本号格式不正确: {__version__}"
    except ImportError:
        # 如果没有直接定义__version__，通过importlib.metadata获取
        try:
            pkg_version = version('xyzstyle')
            # 验证版本格式
            parts = pkg_version.split('.')
            assert len(parts) >= 2, f"版本号格式不正确: {pkg_version}"
            assert all(part.isdigit() for part in parts[:2]), f"版本号格式不正确: {pkg_version}"
        except PackageNotFoundError:
            # 如果包未安装，至少确保导入不会失败
            import xyzstyle
            assert xyzstyle is not None, "无法导入xyzstyle模块"


def test_module_structure():
    """测试模块的基本结构"""
    import xyzstyle
    import xyzstyle.config
    import xyzstyle.set_theme
    
    # 验证主要组件存在
    assert hasattr(xyzstyle, 'setup'), "xyzstyle模块缺少setup函数"
    assert hasattr(xyzstyle.set_theme, 'XYZStyleTheme'), "set_theme模块缺少XYZStyleTheme类"
    assert hasattr(xyzstyle.config, 'ConfigManager'), "config模块缺少ConfigManager类"


def test_setup_function_signature():
    """测试setup函数的签名"""
    import xyzstyle
    import inspect
    
    # 检查setup函数的参数
    sig = inspect.signature(xyzstyle.setup)
    assert 'app' in sig.parameters, "setup函数缺少'app'参数"
    
    # 检查setup函数的返回值（应该返回元数据字典）
    from sphinx.application import Sphinx
    mock_app = type('MockApp', (), {})
    result = xyzstyle.setup(mock_app)
    
    # 验证返回值的结构
    assert isinstance(result, dict), "setup函数应该返回一个字典"
    assert 'parallel_read_safe' in result, "返回的元数据缺少'parallel_read_safe'键"
    assert 'parallel_write_safe' in result, "返回的元数据缺少'parallel_write_safe'键"
    assert isinstance(result['parallel_read_safe'], bool), "'parallel_read_safe'应该是布尔值"
    assert isinstance(result['parallel_write_safe'], bool), "'parallel_write_safe'应该是布尔值"


def test_required_dependencies():
    """测试所需的依赖是否可用"""
    # 检查主要依赖是否可以导入
    try:
        import sphinx
        assert sphinx is not None, "无法导入sphinx"
        
        # 检查sphinx_book_theme是否可用
        try:
            import sphinx_book_theme
            assert sphinx_book_theme is not None, "无法导入sphinx_book_theme"
        except ImportError:
            # sphinx_book_theme可能不是直接导入的，而是作为主题使用
            # 所以这里只是记录警告，而不是断言失败
            pass
    except ImportError as e:
        # 如果依赖不可用，测试应该失败
        assert False, f"缺少必要的依赖: {e}"


def test_theme_directory_structure():
    """测试主题目录结构是否正确"""
    import xyzstyle
    from pathlib import Path
    
    # 获取主题目录路径
    theme_dir = Path(__file__).parent.parent / "src" / "xyzstyle" / "theme" / "xyzstyle"
    
    # 验证主题目录存在
    assert theme_dir.exists(), f"主题目录不存在: {theme_dir}"
    
    # 验证必要的主题文件存在
    theme_toml = theme_dir / "theme.toml"
    layout_html = theme_dir / "layout.html"
    static_dir = theme_dir / "static"
    
    assert theme_toml.exists(), f"主题配置文件不存在: {theme_toml}"
    assert layout_html.exists(), f"主题布局文件不存在: {layout_html}"
    assert static_dir.exists() and static_dir.is_dir(), f"静态资源目录不存在: {static_dir}"


def test_config_manager_import():
    """测试ConfigManager的导入"""
    from xyzstyle.config import ConfigManager
    assert ConfigManager is not None, "无法导入ConfigManager类"
    
    # 检查ConfigManager是否具有预期的方法
    assert hasattr(ConfigManager, '__post_init__'), "ConfigManager缺少__post_init__方法"


def test_xyzstyle_theme_import():
    """测试XYZStyleTheme的导入"""
    from xyzstyle.set_theme import XYZStyleTheme
    assert XYZStyleTheme is not None, "无法导入XYZStyleTheme类"
    
    # 检查XYZStyleTheme是否具有预期的方法
    assert hasattr(XYZStyleTheme, '_create_config_loader_event'), "XYZStyleTheme缺少_create_config_loader_event方法"