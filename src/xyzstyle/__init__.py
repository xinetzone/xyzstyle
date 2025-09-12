"""xyzstyle - A Sphinx theme for documentation.

This module provides a custom Sphinx theme for creating beautiful documentation."""
from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata
from .set_theme import XYZStyleTheme

def setup(app: Sphinx) -> ExtensionMetadata:
    """Set up the xyzstyle Sphinx theme.

    This function is called by Sphinx when the extension is loaded.

    Args:
        app: Sphinx application instance.

    Returns:
        ExtensionMetadata: Dictionary of metadata for the extension.
    """
    XYZStyleTheme(app) # 设置主题
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
