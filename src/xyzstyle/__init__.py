"""xyzstyle - A Sphinx theme for documentation.

This module provides a custom Sphinx theme for creating beautiful, modern documentation.
The theme includes configuration management, styling, and integration with Sphinx.

Attributes:
    setup: The entry point function for the Sphinx extension.
    XYZStyleTheme: The main theme management class.
"""
from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata
from .set_theme import XYZStyleTheme


def setup(app: Sphinx) -> ExtensionMetadata:
    """Set up the xyzstyle Sphinx theme.

    This function is the entry point for the Sphinx extension. It is called by Sphinx
    when the extension is loaded, and it registers the theme and sets up any necessary
    components.

    Args:
        app: Sphinx application instance to which the theme will be added.

    Returns:
        ExtensionMetadata: Dictionary of metadata for the extension indicating parallel
            processing compatibility.
    """
    # Initialize and register the theme with the Sphinx application
    XYZStyleTheme(app)
    
    # Return metadata indicating that the theme is safe for parallel processing
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
