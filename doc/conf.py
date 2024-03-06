# -- Path setup --------------------------------------------------------------
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

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # "sphinxext.rediraffe",
    "sphinx_design",
    "sphinx_copybutton",
    "autoapi.extension",
    # custom extentions
    # "_extension.gallery_directive",
    # "_extension.component_directive",
    # For extension examples and demos
    "myst_nb",
    # "ablog",
    # "jupyter_sphinx",
    # "sphinxcontrib.youtube",
    # "numpydoc",
    # "sphinx_togglebutton",
    "jupyterlite_sphinx",
    # "sphinx_favicon",
]

jupyterlite_config = "jupyterlite_config.json"
# suppress_warnings = ["myst.xref_missing"]
# jupyterlite_contents = f"{ROOT}/tests/lite_contents"
# jupyterlite_bind_ipynb_suffix = False
# jupyterlite_dir = Path("doc/_build/html/lite")

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

# -- Sitemap -----------------------------------------------------------------

# ReadTheDocs has its own way of generating sitemaps, etc.
if not os.environ.get("READTHEDOCS"):
    extensions += ["sphinx_sitemap"]

    html_baseurl = os.environ.get("SITEMAP_URL_BASE", "http://127.0.0.1:8000/")
    sitemap_locales = [None]
    sitemap_url_scheme = "{link}"

# -- MyST options ------------------------------------------------------------

# This allows us to use ::: to denote directives, useful for admonitions
myst_enable_extensions = ["colon_fence", "linkify", "substitution"]
myst_heading_anchors = 2
myst_substitutions = {"rtd": "[Read the Docs](https://readthedocs.org/)"}
# 如果你希望stderr和stdout中的每个输出都被合并成一个流，请使用以下配置。
# 避免将 jupter 执行报错的信息输出到 cmd
nb_merge_streams = True
nb_execution_allow_errors = True
nb_execution_mode = "cache" # 'off'

# nb_mime_priority_overrides = [
#     ('html', 'text/plain', 0),  # 最高级别
#     ('latex', 'image/jpeg', None),  # 禁用
#     # ('*', 'customtype', 20)
# ]

# -- Internationalization ----------------------------------------------------

# specifying the natural language populates some key tags
language = "zh_CN"
# -- 国际化输出 ----------------------------------------------------------------
gettext_compact = False
locale_dirs = ['locales/']

# # -- Ablog options -----------------------------------------------------------

# blog_path = "examples/blog/index"
# blog_authors = {
#     "pydata": ("PyData", "https://pydata.org"),
#     "jupyter": ("Jupyter", "https://jupyter.org"),
# }

# -- Options for HTML output -------------------------------------------------

html_theme = "xyzstyle"
html_logo = "_static/images/logo.jpg"
html_favicon = "_static/images/favicon.jpg"
html_sourcelink_suffix = ""
html_last_updated_fmt = '%Y-%m-%d, %H:%M:%S'  # to reveal the build date in the pages meta

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

# ``pydata-sphinx-theme`` 配置
# Define the json_url for our version switcher.
json_url = 'https://xinetzone.github.io/xyzstyle/_static/switcher.json'

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

html_theme_options = {
    "navigation_with_keys": True,
    "github_url": "https://github.com/xinetzone/xyzstyle",
    "collapse_navigation": True,
    # "external_links": [
    #     {
    #         "url": "https://pydata.org",
    #         "name": "PyData",
    #     },
    #     {
    #         "url": "https://numfocus.org/",
    #         "name": "NumFocus",
    #     },
    #     {
    #         "url": "https://numfocus.org/donate",
    #         "name": "Donate to NumFocus",
    #     },
    # ],
    "header_links_before_dropdown": 4,
    "icon_links": [
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
    ],
    # alternative way to set twitter and github header icons
    # "github_url": "https://github.com/pydata/pydata-sphinx-theme",
    # "twitter_url": "https://twitter.com/PyData",
    # "logo": {
    #     "text": "xyzstyle Theme",
    #     "image_dark": "_static/logo-dark.svg",
    # },
    "use_edit_page_button": True,
    "show_toc_level": 1,
    "navbar_align": "left",  # [left, content, right] For testing that the navbar items align properly
    # # "show_nav_level": 2,
    # "announcement": "https://raw.githubusercontent.com/pydata/pydata-sphinx-theme/main/docs/_templates/custom-template.html",
    # "show_version_warning_banner": True,
    "navbar_center": ["version-switcher", "navbar-nav"],
    # "navbar_start": ["navbar-logo"],
    # "navbar_end": ["theme-switcher", "navbar-icon-links"],
    # "navbar_persistent": ["search-button"],
    # "primary_sidebar_end": ["custom-template", "sidebar-ethical-ads"],
    # "article_footer_items": ["test", "test"],
    # "content_footer_items": ["test", "test"],
    "footer_start": ["copyright"],
    "footer_center": ["sphinx-version"],
    "secondary_sidebar_items": {
        "**/*": ["page-toc", "edit-this-page", "sourcelink"],
        "examples/no-sidebar": [],
    },
    "switcher": {
        "json_url": json_url,
        "version_match": version_match,
    },
    # "back_to_top_button": False,
}

html_sidebars = {
    "contribute/index": [
        "search-field",
        "sidebar-nav-bs",
        "custom-template",
    ],  # This ensures we test for custom sidebars
    "demo/no-sidebar": [],  # Test what page looks like with no sidebar items
}

# _html_sidebars = {
#     "community/index": [
#         "sidebar-nav-bs",
#         "custom-template",
#     ],  # This ensures we test for custom sidebars
#     "examples/no-sidebar": [],  # Test what page looks like with no sidebar items
#     "examples/persistent-search-field": ["search-field"],
#     # Blog sidebars
#     # ref: https://ablog.readthedocs.io/manual/ablog-configuration-options/#blog-sidebars
#     "examples/blog/*": [
#         "ablog/postcard.html",
#         "ablog/recentposts.html",
#         "ablog/tagcloud.html",
#         "ablog/categories.html",
#         "ablog/authors.html",
#         "ablog/languages.html",
#         "ablog/locations.html",
#         "ablog/archives.html",
#     ],
# }

html_context = {
    "github_user": "xinetzone",
    "github_repo": "xyzstyle",
    "github_version": "main",
    "doc_path": "doc",
}

# rediraffe_redirects = {
#     "contributing.rst": "community/index.rst",
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["custom.css", "try_examples.css"]
# html_js_files = ["custom-icon.js"]
todo_include_todos = True

# -- favicon options ---------------------------------------------------------

# # see https://sphinx-favicon.readthedocs.io for more information about the
# # sphinx-favicon extension
# favicons = [
#     # generic icons compatible with most browsers
#     "favicon-32x32.png",
#     "favicon-16x16.png",
#     {"rel": "shortcut icon", "sizes": "any", "href": "favicon.ico"},
#     # chrome specific
#     "android-chrome-192x192.png",
#     # apple icons
#     {"rel": "mask-icon", "color": "#459db9", "href": "safari-pinned-tab.svg"},
#     {"rel": "apple-touch-icon", "href": "apple-touch-icon.png"},
#     # msapplications
#     {"name": "msapplication-TileColor", "content": "#459db9"},
#     {"name": "theme-color", "content": "#ffffff"},
#     {"name": "msapplication-TileImage", "content": "mstile-150x150.png"},
# ]

# -- Options for autosummary/autodoc output ------------------------------------
autosummary_generate = True
autodoc_typehints = "description"
autodoc_member_order = "groupwise"

# -- Options for autoapi -------------------------------------------------------
autoapi_type = "python"
autoapi_dirs = ["../src/xyzstyle"]
autoapi_keep_files = True
autoapi_root = "api"
autoapi_member_order = "groupwise"

# -- application setup -------------------------------------------------------


def setup_to_main(
    app: Sphinx, pagename: str, templatename: str, context, doctree
) -> None:
    """Add a function that jinja can access for returning an "edit this page" link pointing to `main`."""

    def to_main(link: str) -> str:
        """Transform "edit on github" links and make sure they always point to the main branch.

        Args:
            link: the link to the github edit interface

        Returns:
            the link to the tip of the main branch for the same file
        """
        links = link.split("/")
        idx = links.index("edit")
        return "/".join(links[: idx + 1]) + "/main/" + "/".join(links[idx + 2 :])

    context["to_main"] = to_main


def setup(app: Sphinx) -> dict[str, Any]:
    """Add custom configuration to sphinx app.

    Args:
        app: the Sphinx application
    Returns:
        the 2 parallel parameters set to ``True``.
    """
    app.connect("html-page-context", setup_to_main)
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
