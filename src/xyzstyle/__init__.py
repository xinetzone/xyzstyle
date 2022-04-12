"""Sphinx demo."""
from pathlib import Path
import pydata_sphinx_theme

__version__ = '0.0.1'


# def update_context(app, pagename, templatename, context, doctree):
#     context["xyzstyle_version"] = __version__


# def setup(app):
#     here = Path(__file__).parent.resolve()
#     theme_path = here / "themes" / "xyzstyle"
#     app.add_html_theme("xyzstyle", str(theme_path))
#     app.connect("html-page-context", update_context)
#     return {"version": "0.3.0", "parallel_read_safe": True}
# import os

# __version__ = "1.3.1"
# __version_full__ = __version__

def get_html_templates_path(pkg_path=__file__,
                            template_path='../themes/xyzstyle/_templates'):
    """
    Return path to Sphinx templates folder.
    """
    pkgdir = Path(pkg_path).parent
    return str(pkgdir/template_path)

# def get_path():
#     """
#     Shortcut for users whose theme is next to their conf.py.
#     """
#     # Theme directory is defined as our parent directory
#     return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


# def update_context(app, pagename, templatename, context, doctree):
#     context["xyzstyle_version"] = __version_full__


# def setup(app):
#     theme_path = os.path.abspath(os.path.dirname(__file__))
#     app.add_html_theme("xyzstyle", theme_path)
#     app.connect("html-page-context", update_context)
#     return {"version": "0.3.0", "parallel_read_safe": True}
