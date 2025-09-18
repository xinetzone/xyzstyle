from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata
from myst_nb.sphinx_ext import sphinx_setup as setup_myst_nb
from .set_theme import MySTX

def sphinx_setup(app: Sphinx) -> ExtensionMetadata:
    """Sphinx 插件设置函数，用于注册 myst-nb 插件。"""
    setup_myst_nb(app) # Markdown和Jupyter笔记本支持
    MySTX(app) # 自定义主题设置
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
