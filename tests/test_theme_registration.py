import os
import sys
import tempfile
from pathlib import Path
import pytest
from unittest import mock
from sphinx.application import Sphinx

# 添加src目录到路径以便导入xyzstyle模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from xyzstyle.set_theme import XYZStyleTheme
from xyzstyle import setup


@pytest.fixture
def mock_sphinx_app():
    """创建一个模拟的Sphinx应用实例"""
    app = mock.MagicMock(spec=Sphinx)
    app.add_html_theme = mock.MagicMock()
    app.connect = mock.MagicMock()
    return app


def test_xyzstyle_theme_initialization(mock_sphinx_app):
    """测试XYZStyleTheme的初始化过程"""
    # 创建XYZStyleTheme实例
    theme = XYZStyleTheme(mock_sphinx_app)
    
    # 验证主题名称和目录设置正确
    assert theme.name == "xyzstyle"
    assert theme.theme_dir is not None
    assert isinstance(theme.theme_dir, Path)
    
    # 验证主题已注册到Sphinx应用
    mock_sphinx_app.add_html_theme.assert_called_once_with("xyzstyle", theme.theme_dir)
    
    # 验证配置初始化事件已连接
    mock_sphinx_app.connect.assert_called_once()
    assert mock_sphinx_app.connect.call_args[0][0] == 'config-inited'


def test_xyzstyle_theme_inheritance():
    """测试XYZStyle主题的继承关系"""
    # 读取theme.toml文件以验证继承关系
    theme_toml_path = Path(__file__).parent.parent / "src" / "xyzstyle" / "theme" / "xyzstyle" / "theme.toml"
    
    if theme_toml_path.exists():
        with open(theme_toml_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # 验证主题继承自sphinx_book_theme
            assert "inherit = \"sphinx_book_theme\"" in content

@mock.patch('xyzstyle.set_theme.Path')
def test_xyzstyle_theme_invalid_directory(mock_path, mock_sphinx_app):
    """测试XYZStyleTheme处理无效主题目录的情况"""
    # 模拟Path操作以返回不存在的目录
    mock_path_instance = mock.MagicMock()
    mock_path_instance.parent.resolve.return_value = mock.MagicMock()
    mock_path_instance.parent.resolve.return_value.__truediv__.return_value = mock_path_instance
    mock_path_instance.exists.return_value = False
    mock_path.return_value = mock_path_instance
    
    # 初始化应该抛出FileNotFoundError
    with pytest.raises(FileNotFoundError):
        XYZStyleTheme(mock_sphinx_app)

@mock.patch('xyzstyle.set_theme.XYZStyleTheme')
def test_setup_function(mock_xyzstyle_theme, mock_sphinx_app):
    """测试setup函数的功能"""
    # 调用setup函数
    result = setup(mock_sphinx_app)
    
    # 验证XYZStyleTheme被实例化
    mock_xyzstyle_theme.assert_called_once_with(mock_sphinx_app)
    
    # 验证返回的元数据正确
    assert result == {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

@mock.patch('xyzstyle.set_theme.logging.getLogger')
def test_xyzstyle_theme_error_handling(mock_get_logger, mock_sphinx_app):
    """测试XYZStyleTheme的错误处理"""
    # 模拟日志记录器
    mock_logger = mock.MagicMock()
    mock_get_logger.return_value = mock_logger
    
    # 模拟add_html_theme抛出异常
    mock_sphinx_app.add_html_theme.side_effect = Exception("Test registration error")
    
    # 初始化不应抛出异常（错误应被内部捕获并记录）
    theme = XYZStyleTheme(mock_sphinx_app)
    
    # 验证错误被记录
    mock_logger.error.assert_called_once()


def test_create_config_loader_event(mock_sphinx_app):
    """测试_create_config_loader_event方法"""
    theme = XYZStyleTheme(mock_sphinx_app)
    event_handler = theme._create_config_loader_event()
    
    # 验证返回的是可调用对象
    assert callable(event_handler)
    
    # 模拟调用事件处理函数并验证返回值类型
    with mock.patch('xyzstyle.set_theme.ConfigManager') as mock_config_manager:
        mock_config_instance = mock.MagicMock()
        mock_config_manager.return_value = mock_config_instance
        
        result = event_handler(mock_sphinx_app, {})
        
        # 验证ConfigManager被正确实例化
        mock_config_manager.assert_called_once_with(app=mock_sphinx_app, config={})
        # 验证返回了ConfigManager实例
        assert result is mock_config_instance