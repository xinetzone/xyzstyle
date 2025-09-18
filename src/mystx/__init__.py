"""mystx - 基于 sphinx-book-theme 的现代 Sphinx 文档主题

This module provides a custom Sphinx theme for creating beautiful, modern documentation.
The theme includes configuration management, styling, and integration with Sphinx.
"""
from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata


def setup(app: Sphinx) -> ExtensionMetadata:
    """Sphinx extension setup."""
    # we import this locally, so sphinx is not automatically imported
    from .sphinx_ext import sphinx_setup

    return sphinx_setup(app)
