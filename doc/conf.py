"""Sphinx 文档生成器的配置文件。

该文件仅包含最常用选项的配置。完整的选项列表请参阅文档：
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Path setup --------------------------------------------------------------
import sys
from pathlib import Path
import os
from sphinx.locale import _
from typing import Any
from sphinx.application import Sphinx

sys.path.append(str(Path(".").resolve()))
from utils.icon import icon_links

# -- Project information -----------------------------------------------------
project = 'xyzstyle'
copyright = '2022, xinetzone'
author = 'xinetzone'
release = '0.1.0'

# -- 国际化输出 ----------------------------------------------------------------
language = 'zh_CN'
locale_dirs = ['../locales/']  # po files will be created in this directory
gettext_compact = False  # optional: avoid file concatenation in sub directories.

# -- General configuration ---------------------------------------------------
# 在此添加任何 Sphinx 扩展模块名称，以字符串形式表示。
# 它们可以是 Sphinx 自带的扩展（命名为 'sphinx.ext.*'）或您自定义的扩展。
extensions = [
    "ablog",
    "myst_nb",
    "sphinx.ext.napoleon",  # docstring style to support Google style & NumPy
    "numpydoc",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.graphviz",
    "sphinxcontrib.youtube",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_examples",
    "sphinx_tabs.tabs",
    "sphinx_thebe",
    "sphinx_togglebutton",
    "sphinxcontrib.bibtex",
    "sphinxext.opengraph",
    # For the kitchen sink
    "sphinx.ext.todo",
]

# 在此添加包含模板的任何路径，相对于此目录。
templates_path = ['_templates']

# 相对于源目录的模式列表，用于匹配在查找源文件时要忽略的文件和目录。
# 此模式还会影响 html_static_path 和 html_extra_path。
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.12", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "pst": ("https://pydata-sphinx-theme.readthedocs.io/en/latest/", None),
}
nitpick_ignore = [
    ("py:class", "docutils.nodes.document"),
    ("py:class", "docutils.parsers.rst.directives.body.Sidebar"),
]

# application/vnd.plotly.v1+json and application/vnd.bokehjs_load.v0+json
# unknown_mime_type - application/vnd.plotly.v1+json and application/vnd.bokehjs_load.v0+json
# domains - sphinx_proof.domain::prf needs to have `resolve_any_xref` method
# mime_priority - latex priority not set in myst_nb for text/html, application/javascript
suppress_warnings = [
    "mystnb.unknown_mime_type", "mystnb.mime_priority",  # 禁用 application/vnd.plotly.v1+json and application/vnd.bokehjs_load.v0+json 警告
    "myst.xref_missing", "myst.domains", # 禁用 myst 警告
    "ref.ref",
    "autoapi.python_import_resolution", "autoapi.not_readable" # 禁用 autoapi 警告
]

numfig = True

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    # "html_admonition",
    # "html_image",
    "colon_fence",
    # "smartquotes",
    # "replacements",
    # "linkify",
    # "substitution",
]

# -- Options for HTML output -------------------------------------------------
# 用于 HTML 和 HTML Help 页面的主题。
html_theme = "xyzstyle"
html_logo = "_static/images/logo.jpg"
html_title = "Sphinx xyzstyle Theme"
html_copy_source = True
html_favicon = "_static/images/favicon.jpg"
html_last_updated_fmt = '%Y-%m-%d, %H:%M:%S'

# Define the json_url for our version switcher.
json_url = "https://xyzstyle.readthedocs.io/zh-cn/latest/_static/switcher.json"

# Define the version we use for matching in the version switcher.
version_match = os.environ.get("READTHEDOCS_VERSION")
# If READTHEDOCS_VERSION doesn't exist, we're not on RTD
# If it is an integer, we're in a PR build and the version isn't correct.
# If it's "latest" → change to "dev" (that's what we want the switcher to call it)
if not version_match or version_match.isdigit() or version_match == "latest":
    # For local development, infer the version to match from the package.
    if "dev" in release or "rc" in release:
        version_match = "dev"
        # We want to keep the relative reference if we are in dev mode
        # but we want the whole url if we are effectively in a released version
        json_url = "_static/switcher.json"
    else:
        version_match = f"v{release}"
elif version_match == "stable":
    version_match = f"v{release}"

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

# 在此添加包含自定义静态文件（如样式表）的任何路径，相对于此目录。
# 它们会在内置静态文件之后被复制，因此名为 "default.css" 的文件将覆盖内置的 "default.css"。
html_static_path = ['_static']
html_css_files = ["custom.css"]

# 参考 https://myst-nb.readthedocs.io/en/latest/computation/execute.html
nb_execution_mode = "cache"
# nb_execution_excludepatterns = ["ipywidgets/**/**/*.ipynb"]
thebe_config = {
    "repository_url": "https://github.com/xinetzone/xyzstyle",
    "repository_branch": "main",
    "selector": "div.highlight",
    # "selector": ".thebe",
    # "selector_input": "",
    # "selector_output": "",
    # "codemirror-theme": "blackboard",  # Doesn't currently work
    # "always_load": True,  # To load thebe on every page
}

html_theme_options = {
    "path_to_docs": "doc",
    "github_url": "https://github.com/xinetzone/xyzstyle",
    "repository_url": "https://github.com/xinetzone/xyzstyle",
    "repository_branch": "main",
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "colab_url": "https://colab.research.google.com/",
        "deepnote_url": "https://deepnote.com/",
        "notebook_interface": "jupyterlab",
        "thebe": True,
        # "jupyterhub_url": "https://datahub.berkeley.edu",  # For testing
    },
    "use_edit_page_button": True,
    "use_source_button": True,
    "use_issues_button": True,
    # "use_repository_button": True,
    "use_download_button": True,
    "use_sidenotes": True,
    "show_toc_level": 2,
    "announcement": (
        "👋欢迎进入编程视界！👋"
    ),
    # "logo": {
    #     "image_dark": "_static/logo-wide-dark.svg",
    #     # "text": html_title,  # Uncomment to try text with logo
    # },
    "switcher": {
        "json_url": json_url,
        "version_match": version_match,
    },
    "icon_links": icon_links,
    # For testing
    # "use_fullscreen_button": False,
    # "home_page_in_toc": True,
    # "extra_footer": "<a href='https://google.com'>Test</a>",  # DEPRECATED KEY
    # "show_navbar_depth": 2,
    # Testing layout areas
    # "navbar_start": ["test.html"],
    # "navbar_center": ["test.html"],
    # "navbar_end": ["test.html"],
    # "navbar_persistent": ["test.html"],
    # "footer_start": ["test.html"],
    # "footer_end": ["test.html"]
}

# sphinxext.opengraph
ogp_social_cards = {
    "image": "_static/images/logo.jpg",
    "font": "Noto Sans CJK JP", # 支持中文字体
}

# -- Sitemap -----------------------------------------------------------------
# ReadTheDocs has its own way of generating sitemaps, etc.
if not os.environ.get("READTHEDOCS"):
    extensions += ["sphinx_sitemap"]

    html_baseurl = os.environ.get("SITEMAP_URL_BASE", "http://127.0.0.1:8000/")
    sitemap_locales = [None]
    sitemap_url_scheme = "{link}"

# -- sphinx_ext_graphviz options ---------------------------------------------
graphviz_output_format = "svg"
inheritance_graph_attrs = dict(
    rankdir="LR",
    fontsize=14,
    ratio="compress",
)

# -- sphinx_togglebutton options ---------------------------------------------
togglebutton_hint = str(_("Click to expand"))
togglebutton_hint_hide = str(_("Click to collapse"))

# -- sphinx-copybutton config -------------------------------------
# Exclude copy button from appearing over notebook cell numbers by using :not()
# The default copybutton selector is `div.highlight pre`
# https://github.com/executablebooks/sphinx-copybutton/blob/master/sphinx_copybutton/__init__.py#L82
copybutton_exclude = ".linenos, .gp"
copybutton_selector = ":not(.prompt) > div.highlight pre"

# -- ABlog config -------------------------------------------------
blog_path = "reference/blog"
blog_post_pattern = "reference/blog/*.md"
blog_baseurl = "https://xyzstyle.readthedocs.io/zh-cn/latest/"
fontawesome_included = True
post_auto_image = 1
post_auto_excerpt = 2
nb_execution_show_tb = "READTHEDOCS" in os.environ
bibtex_bibfiles = ["references.bib"]
# To test that style looks good with common bibtex config
bibtex_reference_style = "author_year"
bibtex_default_style = "plain"
numpydoc_show_class_members = False  # for automodule:: urllib.parse stub file issue
linkcheck_ignore = [
    "http://someurl/release",  # This is a fake link
    "https://doi.org",  # These don't resolve properly and cause SSL issues
]
linkcheck_exclude_documents = ["changelog"]

# == Napoleon 设置 ==============================================================
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_type_aliases = None
napoleon_attr_annotations = True

# -- autoapi 选项-------------------------------------------------------
autoapi_type = "python"
autoapi_dirs = ["../src/xyzstyle"]
autoapi_keep_files = False # 要开始自己编写 API 文档，你可以让 AutoAPI 保留其生成的文件作为基础
autoapi_root = "api"
autoapi_member_order = "groupwise"

def setup(app):
    # -- To demonstrate ReadTheDocs switcher -------------------------------------
    # This links a few JS and CSS files that mimic the environment that RTD uses
    # so that we can test RTD-like behavior. We don't need to run it on RTD and we
    # don't wanted it loaded in GitHub Actions because it messes up the lighthouse
    # results.
    if not os.environ.get("READTHEDOCS") and not os.environ.get("GITHUB_ACTIONS"):
        app.add_css_file(
            "https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css"
        )
        app.add_css_file("https://assets.readthedocs.org/static/css/badge_only.css")

        # Create the dummy data file so we can link it
        # ref: https://github.com/readthedocs/readthedocs.org/blob/bc3e147770e5740314a8e8c33fec5d111c850498/readthedocs/core/static-src/core/js/doc-embed/footer.js  # noqa: E501
        app.add_js_file("rtd-data.js")
        app.add_js_file(
            "https://assets.readthedocs.org/static/javascript/readthedocs-doc-embed.js",
            priority=501,
        )
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }