import os
import sys
import tempfile
import shutil
from pathlib import Path
import pytest
from sphinx.application import Sphinx

# 添加src目录到路径以便导入xyzstyle模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


@pytest.mark.integration
def test_sphinx_build_with_xyzstyle(temp_doc_project):
    """测试使用XYZStyle主题构建Sphinx文档"""
    # 设置Sphinx构建参数
    src_dir = str(temp_doc_project / "source")
    conf_dir = src_dir
    out_dir = str(temp_doc_project / "build")
    doctree_dir = str(temp_doc_project / "build" / ".doctree")
    buildername = "html"
    status = sys.stdout
    warning = sys.stderr
    
    # 创建Sphinx应用实例
    app = Sphinx(
        srcdir=src_dir,
        confdir=conf_dir,
        outdir=out_dir,
        doctreedir=doctree_dir,
        buildername=buildername,
        status=status,
        warning=warning,
    )
    
    # 初始化应用
    app.initialize()
    
    # 验证主题已正确设置
    assert app.config.html_theme == "xyzstyle"
    
    # 构建文档
    app.build()
    
    # 验证构建输出
    index_html = Path(out_dir) / "index.html"
    assert index_html.exists(), "构建输出文件不存在"
    
    # 检查构建输出中是否包含主题相关的内容
    with open(index_html, 'r', encoding='utf-8') as f:
        content = f.read()
        # 验证是否使用了sphinx_book_theme的结构（因为xyzstyle继承自它）
        assert "<div class=\"sd-content\"" in content


@pytest.mark.integration
def test_config_file_loading():
    """测试从default.toml加载配置"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # 创建临时Sphinx项目结构
        src_dir = Path(temp_dir) / "source"
        src_dir.mkdir()
        
        # 创建default.toml配置文件
        default_toml = src_dir / "default.toml"
        default_toml.write_text("""
[project]
name = "Integration Test Project"
author = "Integration Tester"
version = "1.0.0"
release = "1.0.0"
copyright = "2023 Integration Test Copyright"

[html]
theme = "xyzstyle"
title = "Integration Test Title"
theme_options = {
    "use_download_button" = "True",
    "use_fullscreen_button" = "True",
}
""")
        
        # 创建最小化的conf.py文件
        conf_py = src_dir / "conf.py"
        conf_py.write_text("""
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

# XYZStyle会自动从default.toml加载配置
extensions = [
    'xyzstyle',
]

html_theme = 'xyzstyle'
""")
        
        # 创建index.rst文件
        index_rst = src_dir / "index.rst"
        index_rst.write_text("""
Welcome to Integration Test
==========================

Content here.
""")
        
        # 构建文档
        out_dir = Path(temp_dir) / "build"
        doctree_dir = out_dir / ".doctree"
        
        app = Sphinx(
            srcdir=str(src_dir),
            confdir=str(src_dir),
            outdir=str(out_dir),
            doctreedir=str(doctree_dir),
            buildername="html",
            status=sys.stdout,
            warning=sys.stderr,
        )
        
        # 初始化和构建
        app.initialize()
        app.build()
        
        # 验证构建输出
        index_html = out_dir / "index.html"
        assert index_html.exists()
        
        # 检查是否使用了default.toml中的配置
        with open(index_html, 'r', encoding='utf-8') as f:
            content = f.read()
            assert "Integration Test Title" in content


@pytest.mark.slow
@pytest.mark.integration
def test_theme_customization():
    """测试主题自定义功能"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # 创建临时Sphinx项目
        src_dir = Path(temp_dir) / "source"
        src_dir.mkdir()
        static_dir = src_dir / "_static"
        static_dir.mkdir()
        
        # 创建自定义CSS文件
        custom_css = static_dir / "custom.css"
        custom_css.write_text("""
/* 测试自定义CSS */
.test-custom-class {
    color: #ff0000;
}
""")
        
        # 创建conf.py文件，包含自定义配置
        conf_py = src_dir / "conf.py"
        conf_py.write_text("""
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

project = 'Customization Test'
author = 'Customizer'

html_theme = 'xyzstyle'

extensions = [
    'xyzstyle',
]

html_theme_options = {
    'use_download_button': 'True',
    'use_fullscreen_button': 'True',
}

html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
""")
        
        # 创建包含自定义类的RST文件
        index_rst = src_dir / "index.rst"
        index_rst.write_text("""
Welcome to Customization Test
============================

.. raw:: html

   <div class="test-custom-class">This text should be red</div>
""")
        
        # 构建文档
        out_dir = Path(temp_dir) / "build"
        doctree_dir = out_dir / ".doctree"
        
        app = Sphinx(
            srcdir=str(src_dir),
            confdir=str(src_dir),
            outdir=str(out_dir),
            doctreedir=str(doctree_dir),
            buildername="html",
            status=sys.stdout,
            warning=sys.stderr,
        )
        
        app.initialize()
        app.build()
        
        # 验证构建输出
        index_html = out_dir / "index.html"
        assert index_html.exists()
        
        # 检查自定义CSS是否被包含
        with open(index_html, 'r', encoding='utf-8') as f:
            content = f.read()
            assert "custom.css" in content
            assert "<div class=\"test-custom-class\">" in content