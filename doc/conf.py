# -- init setup --------------------------------------------------------------
import os
import sys
from pathlib import Path
from typing import Any
import xyzstyle
from sphinx.application import Sphinx
os.environ["PYDEVD_DISABLE_FILE_VALIDATION"] = "1"
ROOT = Path('__file__').resolve().parents[1]
sys.path.extend([str(Path(".").resolve()), str(ROOT/'src')])
from utils.icon import icon_links

# -- Project information -----------------------------------------------------

project = 'xyzstyle'
copyright = '2022, xinetzone'
author = 'xinetzone'

# -- Internationalization ----------------------------------------------------
# specifying the natural language populates some key tags
language = "zh_CN"
# -- 国际化输出 ----------------------------------------------------------------
gettext_compact = False
locale_dirs = ['locales/']

# -- Options for HTML output -------------------------------------------------
html_theme = "xyzstyle"
html_logo = "_static/images/logo.jpg"
html_favicon = "_static/images/favicon.jpg"
html_sourcelink_suffix = ""
html_last_updated_fmt = '%Y-%m-%d, %H:%M:%S'  # to reveal the build date in the pages meta

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["custom.css", "try_examples.css"]
# html_js_files = ["custom-icon.js"]
todo_include_todos = True

# Napoleon 设置
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

# -- General configuration ---------------------------------------------------
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build", "Thumbs.db", ".DS_Store", 
    "**.ipynb_checkpoints",
]
# 参考 https://myst-nb.readthedocs.io/en/latest/computation/execute.html
nb_execution_mode = "auto" # "off", "auto", "force", "cache", "inline"
nb_execution_excludepatterns = ["ipywidgets/**/*.ipynb", "ipywidgets/**/**/*.ipynb"]
# intersphinx_mapping = {
#     'python': ('https://daobook.github.io/cpython/', None),
#     'sphinx': ('https://daobook.github.io/sphinx/', None),
#     'peps': ('https://daobook.github.io/peps', None),
# }

# -- Options for autoapi -------------------------------------------------------
autoapi_type = "python"
autoapi_dirs = ["../src/xyzstyle"]
autoapi_keep_files = False # 要开始自己编写 API 文档，你可以让 AutoAPI 保留其生成的文件作为基础
autoapi_root = "api"
autoapi_member_order = "groupwise"

extensions = [
    "xyzstyle",
    "myst_nb",
    # "jupyterlite_sphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "autoapi.extension",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.viewcode",
    "sphinx_thebe",
    # "sphinx_togglebutton",
    # "jupyterlite_sphinx",
    # # "sphinxext.rediraffe",
    # "sphinx.ext.autodoc",
    # "sphinx.ext.autosummary",
    # # custom extentions
    # # "_extension.gallery_directive",
    # # "_extension.component_directive",
    # # For extension examples and demos
    # # "ablog",
    # # "jupyter_sphinx",
    # # "sphinxcontrib.youtube",
    # # "numpydoc",
    # # "sphinx_favicon",
    # "sphinxcontrib.katex",
]
# Define the json_url for our version switcher.
json_url = 'https://xinetzone.github.io/xyzstyle/_static/switcher.json'
# -- Sitemap -----------------------------------------------------------------
# ReadTheDocs has its own way of generating sitemaps, etc.
if not os.environ.get("READTHEDOCS"):
    extensions += ["sphinx_sitemap"]
    html_baseurl = os.environ.get("SITEMAP_URL_BASE", "http://127.0.0.1:8000/")
    sitemap_locales = [None]
    sitemap_url_scheme = "{link}"
# Define the version we use for matching in the version switcher.
version_match = os.environ.get("READTHEDOCS_VERSION")
release = xyzstyle.__version__
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

html_context = {
    "github_user": "xinetzone",
    "github_repo": "xyzstyle",
    "github_version": "main",
    "doc_path": "doc",
}

thebe_config = {
    "repository_url": "https://github.com/xinetzone/xyzstyle",
    "path_to_docs": "doc",
    "repository_branch": "main",
    "selector": "div.highlight",
    # "selector": ".thebe",
    # "selector_input": "",
    # "selector_output": "",
    # "codemirror-theme": "blackboard",  # Doesn't currently work
    # "always_load": True,  # To load thebe on every page
}

# application/vnd.plotly.v1+json and application/vnd.bokehjs_load.v0+json
# unknown_mime_type - application/vnd.plotly.v1+json and application/vnd.bokehjs_load.v0+json
# domains - sphinx_proof.domain::prf needs to have `resolve_any_xref` method
# mime_priority - latex priority not set in myst_nb for text/html, application/javascript
suppress_warnings = [
    "mystnb.unknown_mime_type", "mystnb.mime_priority",  # 禁用 application/vnd.plotly.v1+json and application/vnd.bokehjs_load.v0+json 警告
    "myst.xref_missing", "myst.domains", # 禁用 myst 警告
    "autoapi.python_import_resolution", "autoapi.not_readable" # 禁用 autoapi 警告
]

html_theme_options = {
    "path_to_docs": "doc",
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
    # "show_toc_level": 5,
    "max_navbar_depth": 4,
    "collapse_navbar": False,
    "announcement": (
        "👋欢迎进入编程视界！👋"
    ),
    # "navigation_with_keys": True,
    "switcher": {
        "json_url": json_url,
        "version_match": version_match,
    },
    "icon_links": icon_links,
    # "collapse_navigation": True,
    # "navbar_start": ["test.html"],
    # "navbar_center": ["test.html"],
    # "navbar_end": ["test.html"],
    # "navbar_persistent": ["test.html"],
    # "secondary_sidebar_items": {
    #     "**/*": ["page-toc", "edit-this-page", "sourcelink", ],
    #     "examples/no-sidebar": [],
    # },
    # "primary_sidebar_end": ["sidebar-ethical-ads", ],
    # "article_footer_items": ["test", "test"],
    # "content_footer_items": ["test", "test"],
    "footer_start": ["version-switcher", "copyright"],
    "footer_end": ["sphinx-version", "last-updated"],
}

html_sidebars = {
    # "**/*": ["search-field", "sbt-sidebar-nav.html", "version-switcher", "sidebar-nav-bs",],
    "community/index": [
        "sidebar-nav-bs",
        "custom-template",
    ],  # This ensures we test for custom sidebars
    "examples/no-sidebar": [],  # Test what page looks like with no sidebar items
    "examples/persistent-search-field": ["search-field"],
    # Blog sidebars
    # ref: https://ablog.readthedocs.io/manual/ablog-configuration-options/#blog-sidebars
    "examples/blog/*": [
        "ablog/postcard.html",
        "ablog/recentposts.html",
        "ablog/tagcloud.html",
        "ablog/categories.html",
        "ablog/authors.html",
        "ablog/languages.html",
        "ablog/locations.html",
        "ablog/archives.html",
    ],
}
# html_theme_options = {
#     "launch_buttons": {
#         "binderhub_url": "https://mybinder.org",
#         "colab_url": "https://colab.research.google.com/",
#         "deepnote_url": "https://deepnote.com/",
#         "notebook_interface": "jupyterlab",
#         "thebe": True,
#         # "jupyterhub_url": "https://datahub.berkeley.edu",  # For testing
#     },
# }

# # jupyterlite_dir = ROOT/"tools/lite/apps"
# jupyterlite_contents = "../tests"
# jupyterlite_bind_ipynb_suffix = False
# jupyterlite_config = "jupyterlite_config.json"

def setup(app: Sphinx) -> dict[str, Any]:
    """Add custom configuration to sphinx app.

    Args:
        app: the Sphinx application
    Returns:
        the 2 parallel parameters set to ``True``.
    """
    # app.connect("html-page-context", setup_to_main)
    app.add_object_type('confval', 'confval',
                        objname='configuration value',
                        indextemplate='pair: %s; configuration value')
    # theme_dir = xyzstyle.get_html_theme_path()
    # print(theme_dir.as_posix())
    # app.add_html_theme("xyzstyle", str(theme_dir))
    # # Update templates for sidebar
    # app.config.templates_path.append(str(theme_dir/"_templates"))

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }