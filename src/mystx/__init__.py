"""xyzstyle - A Sphinx theme for documentation.

This module provides a custom Sphinx theme for creating beautiful, modern documentation.
The theme includes configuration management, styling, and integration with Sphinx.

Attributes:
    setup: The entry point function for the Sphinx extension.
    MySTX: The main theme management class.
"""
from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata


def setup(app: Sphinx) -> ExtensionMetadata:
    """Sphinx extension setup."""
    # we import this locally, so sphinx is not automatically imported
    from .sphinx_ext import sphinx_setup

    return sphinx_setup(app)
