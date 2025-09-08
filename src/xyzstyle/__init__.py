from pathlib import Path
from sphinx.util.typing import ExtensionMetadata
from sphinx.application import Sphinx


def get_html_theme_path():
    """Return list of HTML theme paths."""
    parent = Path(__file__).parent.resolve()
    return f"{parent}/theme/xyzstyle"


def setup(app: Sphinx) -> ExtensionMetadata:
    theme_dir = get_html_theme_path()
    app.add_html_theme("xyzstyle", theme_dir)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
