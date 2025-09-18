"""
XYZStyle主题的基础测试

这些测试确保XYZStyle主题的核心功能正常工作。
"""

import pytest
import sys
from pathlib import Path
import importlib
from sphinx.application import Sphinx

# 添加src目录到Python路径以便导入模块
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))


@pytest.fixture
def sphinx_app(tmp_path):
    """创建一个模拟的Sphinx应用实例用于测试"""
    # 创建临时目录作为源目录和输出目录
    src_dir = tmp_path / "src"
    out_dir = tmp_path / "out"
    src_dir.mkdir(exist_ok=True)
    out_dir.mkdir(exist_ok=True)
    
    # 创建最小的conf.py文件
    conf_py = src_dir / "conf.py"
    conf_py.write_text("""project = 'Test Project'
authors = 'Test Author'
html_theme = 'xyzstyle'
""")
    
    # 创建一个简单的index.rst文件
    index_rst = src_dir / "index.rst"
    index_rst.write_text("""Welcome to the Test Project
==================================

This is a test document.
""")
    
    # 创建Sphinx应用实例
    app = Sphinx(
        srcdir=str(src_dir),
        confdir=str(src_dir),
        outdir=str(out_dir),
        doctreedir=str(out_dir / ".doctree"),
        buildername="html",
        status=None,
        warning=None,
        freshenv=True
    )
    
    return app


def test_theme_import():
    """测试xyzstyle主题是否可以正确导入"""
    try:
        import xyzstyle
        assert xyzstyle is not None
    except ImportError:
        pytest.fail("无法导入xyzstyle模块")


def test_setup_function():
    """测试主题的setup函数是否正确定义并可调用"""
    from xyzstyle import setup
    assert callable(setup)


def test_xyzstyle_theme_class():
    """测试XYZStyleTheme类是否正确定义"""
    from xyzstyle.set_theme import XYZStyleTheme
    assert XYZStyleTheme is not None
    assert hasattr(XYZStyleTheme, "__init__")
    assert hasattr(XYZStyleTheme, "__post_init__")


def test_theme_registration(sphinx_app):
    """测试主题是否可以正确注册到Sphinx应用"""
    from xyzstyle.set_theme import XYZStyleTheme
    
    try:
        # 尝试创建并注册主题
        theme = XYZStyleTheme(sphinx_app)
        assert theme.name == "xyzstyle"
        assert theme.theme_dir is not None
        assert Path(theme.theme_dir).exists()
    except Exception as e:
        pytest.fail(f"主题注册失败: {e}")


def test_config_manager():
    """测试ConfigManager类的基本功能"""
    from xyzstyle.set_theme import ConfigManager
    
    # 创建一个模拟的Sphinx应用和配置对象
    class MockConfig:
        def __init__(self):
            self.html_theme_options = {}
    
    class MockApp:
        def __init__(self, srcdir):
            self.srcdir = str(srcdir)
    
    tmp_dir = Path("/tmp/xyzstyle_test")
    tmp_dir.mkdir(exist_ok=True)
    
    try:
        # 测试初始化
        app = MockApp(tmp_dir)
        config = MockConfig()
        config_manager = ConfigManager(app=app, config=config)
        
        assert config_manager.app is app
        assert config_manager.config is config
        
        # 测试不存在的配置文件处理
        default_config = config_manager.load_default_config()
        assert default_config is None
    finally:
        # 清理
        if tmp_dir.exists():
            import shutil
            shutil.rmtree(tmp_dir)


def test_static_files_exist():
    """测试主题的静态文件是否存在"""
    from xyzstyle.set_theme import XYZStyleTheme
    
    # 创建一个简单的模拟app
    class MockApp:
        def add_html_theme(self, name, path):
            pass
        def connect(self, event, handler):
            pass
    
    # 创建主题实例以获取theme_dir
    theme = XYZStyleTheme(MockApp())
    theme_dir = Path(theme.theme_dir)
    
    # 检查关键静态文件是否存在
    assert (theme_dir / "static" / "css" / "custom.css").exists()
    assert (theme_dir / "static" / "css" / "tippy.css").exists()
    assert (theme_dir / "static" / "css" / "try_examples.css").exists()
    assert (theme_dir / "static" / "js" / "custom-icon.js").exists()


def test_theme_toml_exists():
    """测试主题的theme.toml配置文件是否存在"""
    from xyzstyle.set_theme import XYZStyleTheme
    
    # 创建一个简单的模拟app
    class MockApp:
        def add_html_theme(self, name, path):
            pass
        def connect(self, event, handler):
            pass
    
    # 创建主题实例以获取theme_dir
    theme = XYZStyleTheme(MockApp())
    theme_dir = Path(theme.theme_dir)
    
    # 检查theme.toml是否存在
    assert (theme_dir / "theme.toml").exists()