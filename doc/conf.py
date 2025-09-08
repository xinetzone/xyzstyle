"""Sphinx 文档配置文件

此文件配置 xyzstyle 项目的 Sphinx 文档生成选项，包括主题设置、扩展管理、
国际化配置和各种文档功能。
"""

import os
import sys
from pathlib import Path

# 平台特定配置
if sys.platform == 'win32':
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# 设置路径
def get_project_root() -> Path:
    """获取项目根目录路径。"""
    return Path(__file__).resolve().parents[1]

ROOT = get_project_root()
sys.path.extend([str(ROOT/'doc')])

# 导入自定义工具
from utils.links import icon_links


# =============================================================================
# 项目基本信息
# =============================================================================
project = 'xyzstyle'  # 项目名称
copyright = '2022, xinetzone'  # 版权信息
author = 'xinetzone'  # 作者信息


# =============================================================================
# 国际化配置
# =============================================================================
language = 'zh_CN'  # 文档语言
locale_dirs = ['../locales/']  # PO 文件目录
# 禁用子目录中的文件连接，保持各语言文件独立性
gettext_compact = False


# =============================================================================
# Sphinx 扩展配置
# =============================================================================
# 核心扩展列表
initial_extensions = [
    # 内容格式扩展
    "myst_nb",  # Markdown 和 Jupyter Notebook 支持
    "sphinx_design",  # 现代化设计元素
    "sphinx.ext.napoleon",  # 支持 Google 和 NumPy 风格的文档字符串
    
    # 代码相关扩展
    "sphinx.ext.viewcode",  # 源代码查看链接
    "sphinx_copybutton",  # 代码块复制按钮
    
    # 链接和引用扩展
    "sphinx.ext.intersphinx",  # 跨文档链接
    "sphinx.ext.extlinks",  # 短链接支持
    
    # 互动功能扩展
    "sphinx_comments",  # 评论和注释功能
    "sphinx_examples",  # 示例功能
    
    # 自定义扩展
    "_ext.gallery_directive",  # 自定义画廊指令
]

extensions = list(initial_extensions)  # 创建副本以便后续添加扩展


# =============================================================================
# 通用文档配置
# =============================================================================
# 排除文件和目录模式
exclude_patterns = [
    "_build",  # 构建输出目录
    "Thumbs.db",  # 缩略图数据库
    ".DS_Store",  # macOS 系统文件
]

# 交叉引用配置
intersphinx_mapping = {
    "python": ("https://docs.python.org/3.12", None),
    "sphinx": ("https://daobook.github.io/sphinx/", None),
    "pst": ("https://daobook.github.io/pydata-sphinx-theme/", None),
    "sbt": ("https://daobook.github.io/sphinx-book-theme/", None),
    "myst-nb": ("https://daobook.github.io/MyST-NB/", None),
    "myst-parser": ("https://daobook.github.io/MyST-Parser/", None),
}

# 短链接配置
extlinks = {
    'daobook': ('https://daobook.github.io/%s', 'Daobook %s'),
    'xinetzone': ('https://xinetzone.github.io/%s', 'xinetzone %s'),
}


# =============================================================================
# HTML 输出配置
# =============================================================================
# 基本 HTML 设置
html_theme = project  # 使用项目同名主题
html_title = "Sphinx xyzstyle Theme"  # 文档标题
html_static_path = ['_static']  # 静态文件目录
html_logo = "_static/images/logo.jpg"  # Logo 图片
html_favicon = "_static/images/favicon.jpg"  # 图标文件
html_css_files = ["css/custom.css", "css/tippy.css"]  # 自定义 CSS 文件
html_last_updated_fmt = '%Y-%m-%d, %H:%M:%S'  # 最后更新时间格式

# 主题选项配置
html_theme_options = {
    "use_sidenotes": True,  # 启用侧边注释
    "repository_url": f"https://github.com/xinetzone/{project}",  # 仓库链接
    "repository_branch": "main",  # 代码分支
    "path_to_docs": "doc",  # 文档相对路径
    "use_repository_button": True,  # 显示仓库按钮
    "announcement": "👋欢迎进入编程视界！👋",  # 公告横幅
    "back_to_top_button": True,  # 显示返回顶部按钮
    "use_source_button": True,  # 显示查看源代码按钮
    "use_edit_page_button": True,  # 显示编辑页面按钮
    "use_issues_button": True,  # 显示报告问题按钮
    "icon_links": icon_links,  # 图标链接配置
    "primary_sidebar_end": ["version-switcher"],  # 侧边栏底部元素
    # 启动按钮配置
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "colab_url": "https://colab.research.google.com/",
        "deepnote_url": "https://deepnote.com/",
        "notebook_interface": "jupyterlab",
        "thebe": True,
    },
}


# =============================================================================
# 可选功能配置
# =============================================================================
# 1. 代码复制按钮配置
copybutton_exclude = '.linenos, .gp'  # 排除行号和提示符
# 选择器配置，避免复制按钮出现在笔记本单元格编号上
copybutton_selector = ":not(.prompt) > div.highlight pre"

# 2. 评论系统配置
comments_config = {
   "hypothesis": True,  # 启用 Hypothesis 注释
   "utterances": {
      "repo": f"xinetzone/{project}",
      "optional": "config",
   }  # 启用 Utterances 评论
}

# 3. 参考文献配置
extensions.append('sphinxcontrib.bibtex')
bibtex_bibfiles = ['refs.bib']  # BibTeX 文件路径

# 4. API 文档自动生成
extensions.append("autoapi.extension")
autoapi_dirs = [f"../src/"]  # 源代码目录
autoapi_root = "autoapi"  # API 文档输出目录
autoapi_generate_api_docs = True  # 启用 API 文档生成

# 5. 图表生成配置
extensions.append("sphinx.ext.graphviz")
graphviz_output_format = "svg"  # 输出格式
inheritance_graph_attrs = {
    "rankdir": "LR",  # 图表方向：从左到右
    "fontsize": 14,  # 字体大小
    "ratio": "compress",  # 压缩比例
}

# 6. GitHub 贡献者显示
extensions.append('sphinx_contributors')

# 7. 交互式代码功能
extensions.append("sphinx_thebe")
thebe_config = {
    "repository_url": f"https://github.com/xinetzone/{project}",
    "repository_branch": "main",
    "selector": "div.highlight",  # 选择器
}

# 8. 社交媒体预览元数据
extensions.append("sphinxext.opengraph")
ogp_site_url = f"https://{project}.readthedocs.io/zh-cn/latest/"
ogp_social_cards = {
    "site_url": f"{project}.readthedocs.io",
    "image": "_static/images/logo.jpg",
    "font": "Noto Sans CJK JP",  # 支持中文字体
    "line_colors": "#4078c0",
}

# 9. 站点地图生成
extensions.append("sphinx_sitemap")
sitemap_url_scheme = "{lang}{version}{link}"

# 根据环境设置站点 URL
env_github_actions = os.environ.get("GITHUB_ACTIONS")
env_readthedocs = os.environ.get("READTHEDOCS")

sitemap_locales = [None]  # 语言列表
if not env_readthedocs:
    html_baseurl = os.environ.get("SITEMAP_URL_BASE", "http://127.0.0.1:8000/")
    sitemap_url_scheme = "{link}"
elif env_github_actions:
    html_baseurl = os.environ.get("SITEMAP_URL_BASE", "https://xinetzone.github.io/")

# 10. 丰富的悬停提示
extensions.append("sphinx_tippy")
tippy_rtd_urls = [
    "https://docs.readthedocs.io/en/stable/",
    "https://www.sphinx-doc.org/zh-cn/master/",
]

# 11. 版本切换器
extensions.append("_ext.rtd_version")


# =============================================================================
# 高级配置
# =============================================================================
# 忽略特定的 Nitpick 警告
nitpick_ignore = [
    ("py:class", "docutils.nodes.document"),
    ("py:class", "docutils.parsers.rst.directives.body.Sidebar"),
]

# 抑制特定警告
suppress_warnings = [
    "mystnb.unknown_mime_type", "mystnb.mime_priority",
    "myst.xref_missing", "myst.domains",
    "ref.ref",
    "autoapi.python_import_resolution", "autoapi.not_readable",
]

# 启用编号功能
numfig = True

# MyST 扩展配置
myst_enable_extensions = [
    "dollarmath",  # 数学公式支持
    "amsmath",  # 高级数学支持
    "deflist",  # 定义列表
    "colon_fence",  # 冒号分隔的围栏
    "replacements",  # 文本替换
    "substitution",  # 变量替换
]

# 自定义侧边栏
html_sidebars = {
    "reference/blog/*": [
        "navbar-logo.html",
        "search-field.html",
        "ablog/postcard.html",
        "ablog/recentposts.html",
        "ablog/tagcloud.html",
        "ablog/categories.html",
        "ablog/archives.html",
        "sbt-sidebar-nav.html",
    ]
}

