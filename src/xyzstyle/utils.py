import copy
import os
import re
from typing import Any
from docutils.nodes import Node
from sphinx.application import Sphinx
from sphinx.util import logging, matching


def get_theme_options_dict(app: Sphinx) -> dict[str, Any]:
    """Return theme options for the application w/ a fallback if they don't exist.

    The "top-level" mapping (the one we should usually check first, and modify
    if desired) is ``app.builder.theme_options``. It is created by Sphinx as a
    copy of ``app.config.html_theme_options`` (containing user-configs from
    their ``conf.py``); sometimes that copy never occurs though which is why we
    check both.
    """
    if hasattr(app.builder, "theme_options"):
        return app.builder.theme_options
    elif hasattr(app.config, "html_theme_options"):
        return app.config.html_theme_options
    else:
        return {}

def config_provided_by_user(app: Sphinx, key: str) -> bool:
    """Check if the user has manually provided the config."""
    return any(key in ii for ii in [app.config.overrides, app.config._raw_config])

SPHINX_LOGGER = logging.getLogger(__name__)


def maybe_warn(app: Sphinx, msg, *args, **kwargs):
    """Wraps the Sphinx logger to allow warning suppression."""
    theme_options = get_theme_options_dict(app)
    should_warn = theme_options.get("surface_warnings", False)
    if should_warn:
        SPHINX_LOGGER.warning(msg, *args, **kwargs)
    else:
        SPHINX_LOGGER.info(msg, *args, **kwargs)
