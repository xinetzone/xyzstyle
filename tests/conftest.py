import os
import sys
import pytest
from pathlib import Path

# 添加src目录到路径以便在所有测试中导入xyzstyle模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


@pytest.fixture(scope="session")
def project_root():
    """返回项目根目录的路径"""
    return Path(__file__).parent.parent


@pytest.fixture(scope="session")
def src_dir(project_root):
    """返回源码目录的路径"""
    return project_root / "src"


@pytest.fixture(scope="session")
def theme_dir(src_dir):
    """返回主题目录的路径"""
    return src_dir / "xyzstyle" / "theme" / "xyzstyle"


@pytest.fixture
def temp_doc_project(tmp_path):
    """创建一个临时的Sphinx文档项目结构"""
    # 创建基本目录结构
    (tmp_path / "source").mkdir()
    (tmp_path / "build").mkdir()
    
    # 创建示例配置文件
    conf_py = tmp_path / "source" / "conf.py"
    conf_py.write_text("""
# -*- coding: utf-8 -*-
project = 'Test Project'
author = 'Test Author'
version = '0.1'
release = '0.1.0'

extensions = [
    'xyzstyle',
]

html_theme = 'xyzstyle'
html_theme_options = {
    'use_download_button': 'True',
    'use_fullscreen_button': 'True',
}
""")
    
    # 创建示例index.rst文件
    index_rst = tmp_path / "source" / "index.rst"
    index_rst.write_text("""
Welcome to Test Project's documentation!
========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
""")
    
    return tmp_path


@pytest.fixture
def mock_sphinx_app(mocker):
    """创建一个模拟的Sphinx应用实例"""
    from sphinx.application import Sphinx
    app = mocker.MagicMock(spec=Sphinx)
    app.srcdir = os.getcwd()
    app.add_html_theme = mocker.MagicMock()
    app.connect = mocker.MagicMock()
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


# 添加命令行选项
def pytest_addoption(parser):
    parser.addoption(
        "--run-slow", action="store_true", default=False,
        help="运行慢速测试"
    )
    parser.addoption(
        "--run-integration", action="store_true", default=False,
        help="运行集成测试"
    )


# 注册标记
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "slow: 标记慢速测试"
    )
    config.addinivalue_line(
        "markers", "integration: 标记集成测试"
    )


# 根据命令行选项跳过测试
def pytest_collection_modifyitems(config, items):
    if not config.getoption("--run-slow"):
        skip_slow = pytest.mark.skip(reason="需要 --run-slow 选项来运行")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skip_slow)
    
    if not config.getoption("--run-integration"):
        skip_integration = pytest.mark.skip(reason="需要 --run-integration 选项来运行")
        for item in items:
            if "integration" in item.keywords:
                item.add_marker(skip_integration)