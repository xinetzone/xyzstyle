# -- init setup --------------------------------------------------------------
import os
import sys
from pathlib import Path
from typing import Any
import xyzstyle
from sphinx.application import Sphinx

ROOT = Path('__file__').resolve().parents[1]
sys.path.extend([str(Path(".").resolve()), str(ROOT/'src')])

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
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]
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
    "jupyterlite_sphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "autoapi.extension",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.viewcode",
    "sphinx_thebe",
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
    "show_toc_level": 2,
    "announcement": (
        "⚠️The latest release refactored our HTML, "
        "so double-check your custom CSS rules!⚠️"
    ),
    "navigation_with_keys": True,
    "switcher": {
        "json_url": json_url,
        "version_match": version_match,
    },
    "collapse_navigation": False,
    "navbar_align": "content",  # "right", "left", "content"
    # "navbar_start": "navbar-logo.html",
    "navbar_center": "navbar-nav.html",
    "navbar_end": ["theme-switcher", "version-switcher", "navbar-icon-links"],
    # "secondary_sidebar_items": ["page-toc.html", "edit-this-page.html"],
    "footer_start": ["copyright", "sphinx-version"],
    "footer_end": ["last-updated", ],
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

html_theme_options["icon_links"] = [
    # {
    #     "name": "GitHub",
    #     "url": "https://github.com/xinetzone/tvm-book",
    #     "icon": "fa-brands fa-square-github",
    #     "type": "fontawesome",
    # },
    {
        "name": "知乎",
        "url": "https://www.zhihu.com/people/xinetzone",
        "icon": "fa-brands fa-zhihu",
        "type": "fontawesome",
    },
    {
        "name": "简书",
        "url": "https://www.jianshu.com/u/4302480a3e8e",
        "icon": "fa-solid fa-book",
        "type": "fontawesome",
    },
    {
        "name": "B站",
        "url": "https://space.bilibili.com/252192181",
        "icon": "fa-brands fa-bilibili",
        "type": "fontawesome",
    },
    {
        "name": "博客园",
        "url": "https://www.cnblogs.com/q735613050/",
        "icon": "https://xinetzone.github.io/xinetzone/media/xinetzone.jpg",
        "type": "url",
    },
    {
        "name": "领英",
        "url": "https://www.linkedin.com/in/xinet",
        "icon": "fa-brands fa-linkedin",
        "type": "fontawesome",
    },
    # {
    #     "name": "GitLab",
    #     "url": "https://gitlab.com/<your-org>/<your-repo>",
    #     "icon": "fa-brands fa-square-gitlab",
    #     "type": "fontawesome",
    # },
    # {
    #     "name": "Twitter",
    #     "url": "https://twitter.com/<your-handle>",
    #     "icon": "fa-brands fa-square-twitter",
    #     # The default for `type` is `fontawesome` so it is not actually required in any of the above examples as it is shown here
    # },
    # {
    #     "name": "Mastodon",
    #     "url": "https://<your-host>@<your-handle>",
    #     "icon": "fa-brands fa-mastodon",
    # },
    # {
    #     "name": "PyData",
    #     "url": "https://pydata.org",
    #     "icon": "_static/pydata-logo.png",
    #     "type": "local",
    #     "attributes": {"target": "_blank"},
    # },
]

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