"""Sphinx demo."""
from pathlib import Path
import pydata_sphinx_theme

__version__ = '0.0.1'
__version_full__ = __version__


def get_html_theme_path():
    """
    Return path to Sphinx templates folder.
    """
    parent = Path(__file__).parents[1].resolve()
    theme_path = parent / "themes" / "xyzstyle"
    return theme_path

def get_html_template_path():
    theme_dir = get_html_theme_path()
    return str(theme_dir/"_templates")


def update_context(app, pagename, templatename, context, doctree):
    context["xyzstyle_version"] = __version_full__


def setup(app):
    theme_dir = get_html_theme_path()
    app.add_html_theme("xyzstyle", str(theme_dir))
    app.connect("html-page-context", update_context)
    # Update templates for sidebar
    app.config.templates_path.append(str(theme_dir/"_templates"))
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
