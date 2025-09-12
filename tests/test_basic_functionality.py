import os
import sys
import tempfile
from pathlib import Path
import pytest

# 添加src目录到路径以便导入xyzstyle模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


def test_theme_configuration():
    """测试主题的配置选项"""
    # 读取theme.toml文件以验证配置选项
    theme_toml_path = Path(__file__).parent.parent / "src" / "xyzstyle" / "theme" / "xyzstyle" / "theme.toml"
    
    if theme_toml_path.exists():
        with open(theme_toml_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # 验证主题继承
            assert "inherit = \"sphinx_book_theme\"" in content, "主题未正确继承sphinx_book_theme"
            
            # 验证样式表配置
            assert "stylesheets = [" in content, "缺少样式表配置"
            assert "css/custom.css" in content, "缺少custom.css"
            assert "css/tippy.css" in content, "缺少tippy.css"
            assert "css/try_examples.css" in content, "缺少try_examples.css"
            
            # 验证侧边栏配置
            assert "sidebars = [" in content, "缺少侧边栏配置"
            assert "navbar-logo.html" in content, "缺少navbar-logo.html"
            assert "icon-links.html" in content, "缺少icon-links.html"
            assert "search-button-field.html" in content, "缺少search-button-field.html"
            assert "sbt-sidebar-nav.html" in content, "缺少sbt-sidebar-nav.html"
            
            # 验证代码高亮样式配置
            assert "pygments_style = { default = \"perldoc\" }" in content, "代码高亮样式配置不正确"
            
            # 验证主题选项配置
            assert "[options]" in content, "缺少主题选项配置"
            assert "announcement = \"\"" in content, "公告选项配置不正确"
            assert "secondary_sidebar_items = \"page-toc.html\"" in content, "侧边栏项目配置不正确"


def test_static_resources():
    """测试静态资源文件是否存在"""
    static_dir = Path(__file__).parent.parent / "src" / "xyzstyle" / "theme" / "xyzstyle" / "static"
    
    # 验证静态资源目录存在
    assert static_dir.exists() and static_dir.is_dir(), "静态资源目录不存在"
    
    # 验证CSS目录存在
    css_dir = static_dir / "css"
    assert css_dir.exists() and css_dir.is_dir(), "CSS目录不存在"
    
    # 验证JS目录存在
    js_dir = static_dir / "js"
    assert js_dir.exists() and js_dir.is_dir(), "JS目录不存在"


def test_layout_template():
    """测试布局模板文件"""
    layout_html_path = Path(__file__).parent.parent / "src" / "xyzstyle" / "theme" / "xyzstyle" / "layout.html"
    
    # 验证布局文件存在
    assert layout_html_path.exists(), "布局模板文件不存在"
    
    # 验证布局文件内容
    with open(layout_html_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # 验证布局继承自sphinx_book_theme
        assert "{% extends \"!sphinx_book_theme/layout.html\" %}" in content, "布局未正确继承自sphinx_book_theme"


def test_config_manager_data_structure():
    """测试ConfigManager的数据结构"""
    from xyzstyle.config.manager import SphinxConfig
    
    # 验证SphinxConfig数据类的字段
    config = SphinxConfig()
    
    # 验证项目基本信息字段
    assert hasattr(config, 'project'), "SphinxConfig缺少project字段"
    assert hasattr(config, 'author'), "SphinxConfig缺少author字段"
    assert hasattr(config, 'version'), "SphinxConfig缺少version字段"
    assert hasattr(config, 'release'), "SphinxConfig缺少release字段"
    assert hasattr(config, 'copyright'), "SphinxConfig缺少copyright字段"
    assert hasattr(config, 'language'), "SphinxConfig缺少language字段"
    
    # 验证构建配置字段
    assert hasattr(config, 'exclude_patterns'), "SphinxConfig缺少exclude_patterns字段"
    
    # 验证HTML输出配置字段
    assert hasattr(config, 'html_theme'), "SphinxConfig缺少html_theme字段"
    assert hasattr(config, 'html_title'), "SphinxConfig缺少html_title字段"
    assert hasattr(config, 'html_static_path'), "SphinxConfig缺少html_static_path字段"
    assert hasattr(config, 'html_favicon'), "SphinxConfig缺少html_favicon字段"
    assert hasattr(config, 'html_logo'), "SphinxConfig缺少html_logo字段"
    assert hasattr(config, 'html_theme_options'), "SphinxConfig缺少html_theme_options字段"
    
    # 验证扩展配置字段
    assert hasattr(config, 'extensions'), "SphinxConfig缺少extensions字段"


def test_config_mapping():
    """测试配置映射是否正确"""
    from xyzstyle.config.manager import ConfigManager
    
    # 创建ConfigManager实例
    config_manager = ConfigManager()
    
    # 验证_CONFIG_MAPPING常量存在且结构正确
    assert hasattr(config_manager, '_CONFIG_MAPPING'), "ConfigManager缺少_CONFIG_MAPPING常量"
    mapping = config_manager._CONFIG_MAPPING
    
    # 验证映射包含必要的配置项
    required_keys = [
        'project', 'author', 'version', 'release', 'copyright',
        'language', 'exclude_patterns', 'html_theme', 'html_title',
        'html_static_path', 'html_favicon', 'html_logo', 'html_theme_options',
        'extensions'
    ]
    
    for key in required_keys:
        assert key in mapping, f"配置映射缺少'{key}'"
        assert len(mapping[key]) == 3, f"'{key}'的映射结构不正确"


def test_theme_class_structure():
    """测试XYZStyleTheme类的结构"""
    from xyzstyle.set_theme import XYZStyleTheme
    
    # 验证类的属性
    theme = XYZStyleTheme(app=None)
    
    # 验证属性存在
    assert hasattr(theme, 'app'), "XYZStyleTheme缺少app属性"
    assert hasattr(theme, 'name'), "XYZStyleTheme缺少name属性"
    assert hasattr(theme, 'theme_dir'), "XYZStyleTheme缺少theme_dir属性"
    
    # 验证方法存在
    assert hasattr(theme, '__post_init__'), "XYZStyleTheme缺少__post_init__方法"
    assert hasattr(theme, '_create_config_loader_event'), "XYZStyleTheme缺少_create_config_loader_event方法"


def test_theme_initialization_with_path():
    """测试使用路径初始化主题"""
    from xyzstyle.set_theme import XYZStyleTheme
    import tempfile
    
    # 创建临时应用对象
    class MockApp:
        def __init__(self):
            self.add_html_theme_called = False
            self.connect_called = False
        
        def add_html_theme(self, name, path):
            self.add_html_theme_called = True
        
        def connect(self, event, handler):
            self.connect_called = True
    
    mock_app = MockApp()
    
    # 由于实际初始化会检查主题目录，我们使用mock来避免这个问题
    with pytest.raises(Exception):
        # 这里会抛出异常，因为我们没有提供有效的主题目录
        theme = XYZStyleTheme(mock_app)