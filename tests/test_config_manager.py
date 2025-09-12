import os
import sys
import tempfile
from pathlib import Path
import pytest
from unittest import mock
from sphinx.application import Sphinx

# 添加src目录到路径以便导入xyzstyle模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from xyzstyle.config.manager import ConfigManager, ConfigValidationError


@pytest.fixture
def mock_sphinx_app():
    """创建一个模拟的Sphinx应用实例"""
    app = mock.MagicMock(spec=Sphinx)
    app.srcdir = os.getcwd()
    return app


@pytest.fixture
def mock_config():
    """创建一个模拟的Sphinx配置对象"""
    return {
        'project': 'Test Project',
        'author': 'Test Author',
        'version': '0.1.0',
        'release': '0.1.0',
        'copyright': '2023 Test Copyright',
        'language': 'en',
        'exclude_patterns': [],
        'html_theme': 'xyzstyle',
        'html_title': 'Test Title',
        'html_static_path': ['_static'],
        'html_favicon': None,
        'html_logo': None,
        'html_theme_options': {},
        'extensions': []
    }


def test_config_manager_initialization(mock_sphinx_app, mock_config):
    """测试ConfigManager的初始化"""
    config_manager = ConfigManager(app=mock_sphinx_app, config=mock_config)
    assert config_manager.app is mock_sphinx_app
    assert config_manager.config is mock_config
    assert config_manager.updated_count == 0
    assert isinstance(config_manager.config_path, Path)


def test_config_manager_with_direct_path():
    """测试ConfigManager直接通过路径加载配置"""
    # 创建临时TOML配置文件
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_config = Path(temp_dir) / "test_config.toml"
        temp_config.write_text("""
[project]
name = "Test Project"
author = "Test Author"
version = "1.0.0"
release = "1.0.0"
copyright = "2023 Test Copyright"

[html]
theme = "xyzstyle"
title = "Test Title"
""")
        
        # 通过直接路径初始化ConfigManager
        config_manager = ConfigManager(_direct_path=str(temp_config))
        assert config_manager._data is not None
        assert "project" in config_manager._data
        assert "html" in config_manager._data

@mock.patch('xyzstyle.config.manager.tomllib.load')
def test_config_manager_load_error(mock_tomllib_load, mock_sphinx_app, mock_config):
    """测试ConfigManager加载配置时出现错误的情况"""
    # 模拟tomllib.load抛出异常
    mock_tomllib_load.side_effect = Exception("Test error")
    
    # 初始化ConfigManager不应抛出异常（错误应被内部捕获）
    config_manager = ConfigManager(app=mock_sphinx_app, config=mock_config)
    # 验证错误被正确处理
    assert config_manager._data == {}


def test_config_manager_create_config_loader_event(mock_sphinx_app, mock_config):
    """测试ConfigManager创建配置加载器事件处理函数"""
    from xyzstyle.set_theme import XYZStyleTheme
    
    theme = XYZStyleTheme(mock_sphinx_app)
    event_handler = theme._create_config_loader_event()
    
    # 调用事件处理函数应该返回ConfigManager实例
    result = event_handler(mock_sphinx_app, mock_config)
    assert isinstance(result, ConfigManager)


def test_config_manager_with_missing_file(mock_sphinx_app, mock_config):
    """测试ConfigManager处理不存在的配置文件"""
    # 创建一个指向不存在文件的临时目录
    with tempfile.TemporaryDirectory() as temp_dir:
        # 修改app的srcdir指向临时目录
        mock_sphinx_app.srcdir = temp_dir
        
        # 初始化ConfigManager不应抛出异常
        config_manager = ConfigManager(app=mock_sphinx_app, config=mock_config)
        # 验证_config_path指向了不存在的文件
        assert not config_manager.config_path.exists()