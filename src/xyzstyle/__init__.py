"""xyzstyle - A Sphinx theme for documentation.

This module provides a custom Sphinx theme for creating beautiful documentation.
"""

from pathlib import Path
from typing import Any, Dict

from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata

def get_html_theme_path() -> str:
    """Return the path to the HTML theme directory.

    Returns:
        str: Absolute path to the theme directory.
    """
    parent = Path(__file__).parent.resolve()
    return f"{parent}/theme/xyzstyle"

def setup(app: Sphinx) -> ExtensionMetadata:
    """Set up the xyzstyle Sphinx theme.

    This function is called by Sphinx when the extension is loaded.

    Args:
        app: Sphinx application instance.

    Returns:
        ExtensionMetadata: Dictionary of metadata for the extension.
    """
    theme_dir = get_html_theme_path()
    app.add_html_theme("xyzstyle", theme_dir)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
