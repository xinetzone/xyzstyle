import os
import sys
import tempfile
from pathlib import Path
import pytest
from unittest import mock

# 添加src目录到路径以便导入xyzstyle模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


class MockSphinxApp:
    """模拟Sphinx应用对象"""
    def __init__(self):
        self.config = {}
        self.builder = mock.MagicMock()
        self.builder.outdir = tempfile.gettempdir()

    def add_html_theme(self, name, path):
        pass

    def connect(self, event, callback):
        # 保存回调函数以便后续调用
        setattr(self, f"_callback_{event}", callback)

    def trigger_event(self, event, *args):
        # 模拟触发事件
        callback = getattr(self, f"_callback_{event}", None)
        if callback:
            return callback(self, *args)
        return []


class TestConfigLoading:
    """测试配置加载功能"""
    
    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.mock_app = MockSphinxApp()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.temp_dir.name)
        
    def teardown_method(self):
        """每个测试方法执行后的清理"""
        self.temp_dir.cleanup()

    def create_test_config(self, content):
        """创建测试配置文件"""
        config_path = self.temp_path / "pyproject.toml"
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return config_path

    def test_valid_config_loading(self):
        """测试加载有效的配置文件"""
        from xyzstyle.config.manager import ConfigManager
        
        # 创建有效的配置文件
        valid_config = """
        [project]
        name = "Test Project"
        authors = [
            { name = "Test Author", email = "test@example.com" }
        ]
        version = "1.0.0"
        
        [tool.xyzstyle]
        html_theme = "xyzstyle"
        html_title = "Test Documentation"
        language = "zh_CN"
        """
        
        config_path = self.create_test_config(valid_config)
        
        # 创建ConfigManager并加载配置
        config_manager = ConfigManager()
        config = config_manager.load_config(str(config_path))
        
        # 验证加载的配置
        assert config.project == "Test Project"
        assert config.author == "Test Author"
        assert config.version == "1.0.0"
        assert config.release == "1.0.0"
        assert config.html_theme == "xyzstyle"
        assert config.html_title == "Test Documentation"
        assert config.language == "zh_CN"

    def test_config_loading_with_theme_options(self):
        """测试加载包含主题选项的配置文件"""
        from xyzstyle.config.manager import ConfigManager
        
        # 创建包含主题选项的配置文件
        config_with_theme_options = """
        [project]
        name = "Test Project"
        authors = [
            { name = "Test Author", email = "test@example.com" }
        ]
        version = "1.0.0"
        
        [tool.xyzstyle]
        html_theme = "xyzstyle"
        
        [tool.xyzstyle.html_theme_options]
        announcement = "Welcome to Test Documentation"
        secondary_sidebar_items = "page-toc.html"
        repository_url = "https://github.com/example/test"
        """
        
        config_path = self.create_test_config(config_with_theme_options)
        
        # 创建ConfigManager并加载配置
        config_manager = ConfigManager()
        config = config_manager.load_config(str(config_path))
        
        # 验证主题选项
        assert config.html_theme_options["announcement"] == "Welcome to Test Documentation"
        assert config.html_theme_options["secondary_sidebar_items"] == "page-toc.html"
        assert config.html_theme_options["repository_url"] == "https://github.com/example/test"

    def test_config_loading_with_extensions(self):
        """测试加载包含扩展的配置文件"""
        from xyzstyle.config.manager import ConfigManager
        
        # 创建包含扩展的配置文件
        config_with_extensions = """
        [project]
        name = "Test Project"
        authors = [
            { name = "Test Author", email = "test@example.com" }
        ]
        version = "1.0.0"
        
        [tool.xyzstyle]
        html_theme = "xyzstyle"
        extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
        """
        
        config_path = self.create_test_config(config_with_extensions)
        
        # 创建ConfigManager并加载配置
        config_manager = ConfigManager()
        config = config_manager.load_config(str(config_path))
        
        # 验证扩展
        assert "sphinx.ext.autodoc" in config.extensions
        assert "sphinx.ext.napoleon" in config.extensions

    def test_config_loading_missing_tool_section(self):
        """测试加载缺少tool.xyzstyle部分的配置文件"""
        from xyzstyle.config.manager import ConfigManager
        
        # 创建缺少tool.xyzstyle部分的配置文件
        config_missing_tool_section = """
        [project]
        name = "Test Project"
        authors = [
            { name = "Test Author", email = "test@example.com" }
        ]
        version = "1.0.0"
        """
        
        config_path = self.create_test_config(config_missing_tool_section)
        
        # 创建ConfigManager并加载配置
        config_manager = ConfigManager()
        config = config_manager.load_config(str(config_path))
        
        # 验证默认配置
        assert config.project == "Test Project"
        assert config.author == "Test Author"
        assert config.version == "1.0.0"
        assert config.html_theme == "xyzstyle"  # 默认值

    def test_config_loading_invalid_file(self):
        """测试加载无效的配置文件"""
        from xyzstyle.config.manager import ConfigManager
        
        # 创建无效的TOML文件
        invalid_config = """
        This is not a valid TOML file
        project.name = "Test Project"
        """
        
        config_path = self.create_test_config(invalid_config)
        
        # 创建ConfigManager并尝试加载配置，应该抛出异常
        config_manager = ConfigManager()
        with pytest.raises(Exception):
            config_manager.load_config(str(config_path))

    def test_config_loading_non_existent_file(self):
        """测试加载不存在的配置文件"""
        from xyzstyle.config.manager import ConfigManager
        
        # 创建不存在的文件路径
        non_existent_path = self.temp_path / "non_existent.toml"
        
        # 创建ConfigManager并尝试加载配置，应该抛出异常
        config_manager = ConfigManager()
        with pytest.raises(FileNotFoundError):
            config_manager.load_config(str(non_existent_path))

    def test_config_loading_with_default_values(self):
        """测试配置加载的默认值"""
        from xyzstyle.config.manager import ConfigManager, SphinxConfig
        
        # 创建一个空的配置文件
        empty_config = """
        [project]
        name = "Test Project"
        """
        
        config_path = self.create_test_config(empty_config)
        
        # 创建ConfigManager并加载配置
        config_manager = ConfigManager()
        config = config_manager.load_config(str(config_path))
        
        # 创建默认配置用于比较
        default_config = SphinxConfig()
        
        # 验证未设置的字段使用默认值
        assert config.language == default_config.language
        assert config.exclude_patterns == default_config.exclude_patterns
        assert config.html_static_path == default_config.html_static_path
        assert config.html_theme == default_config.html_theme

    def test_config_apply_to_sphinx(self):
        """测试将配置应用到Sphinx应用"""
        from xyzstyle.config.manager import ConfigManager
        
        # 创建测试配置
        test_config = """
        [project]
        name = "Test Project"
        authors = [
            { name = "Test Author", email = "test@example.com" }
        ]
        version = "1.0.0"
        
        [tool.xyzstyle]
        html_theme = "xyzstyle"
        html_title = "Test Documentation"
        language = "zh_CN"
        """
        
        config_path = self.create_test_config(test_config)
        
        # 创建ConfigManager并加载配置
        config_manager = ConfigManager()
        config = config_manager.load_config(str(config_path))
        
        # 应用配置到模拟的Sphinx应用
        config_manager.apply_config(self.mock_app, config)
        
        # 验证配置是否正确应用
        assert self.mock_app.config["project"] == "Test Project"
        assert self.mock_app.config["author"] == "Test Author"
        assert self.mock_app.config["version"] == "1.0.0"
        assert self.mock_app.config["html_theme"] == "xyzstyle"
        assert self.mock_app.config["html_title"] == "Test Documentation"
        assert self.mock_app.config["language"] == "zh_CN"

    @mock.patch('xyzstyle.config.manager.Path')
    def test_config_auto_discovery(self, mock_path):
        """测试配置文件自动发现功能"""
        from xyzstyle.config.manager import ConfigManager
        
        # 设置mock行为
        mock_path_obj = mock.MagicMock()
        mock_path_obj.exists.return_value = True
        mock_path.return_value = mock_path_obj
        
        # 创建ConfigManager
        config_manager = ConfigManager()
        
        # 调用auto_discover_config方法
        with mock.patch.object(config_manager, 'load_config') as mock_load_config:
            config_manager.auto_discover_config("/some/path")
            
            # 验证是否正确检查了可能的配置文件路径
            assert mock_path.called
            # 验证是否调用了load_config
            assert mock_load_config.called

    def test_integration_with_theme_loader(self):
        """测试与主题加载器的集成"""
        from xyzstyle.set_theme import XYZStyleTheme
        from xyzstyle.config.manager import ConfigManager
        
        # 创建测试配置
        test_config = """
        [project]
        name = "Test Project"
        authors = [
            { name = "Test Author", email = "test@example.com" }
        ]
        version = "1.0.0"
        
        [tool.xyzstyle]
        html_theme = "xyzstyle"
        """
        
        config_path = self.create_test_config(test_config)
        
        # 设置环境变量指向配置文件
        os.environ["XYZSTYLE_CONFIG"] = str(config_path)
        
        try:
            # 创建主题对象，这应该触发配置加载
            with mock.patch('xyzstyle.set_theme.ConfigManager') as mock_config_manager:
                mock_instance = mock.MagicMock()
                mock_config_manager.return_value = mock_instance
                
                theme = XYZStyleTheme(self.mock_app)
                
                # 验证是否创建了配置加载器事件
                assert hasattr(self.mock_app, '_callback_config-inited')
        finally:
            # 清理环境变量
            os.environ.pop("XYZSTYLE_CONFIG", None)