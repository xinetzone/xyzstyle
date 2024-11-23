"""Sphinx demo."""
from pathlib import Path
import sys
import json

from functools import partial
from pathlib import Path
from urllib.parse import urlparse
import requests
from requests.exceptions import ConnectionError, HTTPError, RetryError
from sphinx.errors import ExtensionError
from . import utils

if sys.platform == 'win32':
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

__version__ = '0.0.9'
__version_full__ = __version__


def get_html_theme_path():
    """
    Return path to Sphinx templates folder.
    """
    parent = Path(__file__).parent.resolve()
    theme_path = parent / "themes" / "xyzstyle"
    return theme_path


def get_html_template_path():
    theme_dir = get_html_theme_path()
    return theme_dir/"_templates"


def update_context(app, pagename, templatename, context, doctree):
    context["xyzstyle_version"] = __version_full__


def update_config(app):
    """Update config with new default values and handle deprecated keys."""
    # By the time `builder-inited` happens, `app.builder.theme_options` already exists.
    # At this point, modifying app.config.html_theme_options will NOT update the
    # page's HTML context (e.g. in jinja, `theme_keyword`).
    # To do this, you must manually modify `app.builder.theme_options`.
    theme_options = utils.get_theme_options_dict(app)
    warning = partial(utils.maybe_warn, app)

    # TODO: DEPRECATE after v1.0
    themes = ["light", "dark"]
    for theme in themes:
        if style := theme_options.get(f"pygment_{theme}_style"):
            theme_options[f"pygments_{theme}_style"] = style
            warning(
                f'The parameter "pygment_{theme}_style" was renamed to '
                f'"pygments_{theme}_style" (note the "s" on "pygments").'
            )

    # Validate icon links
    if not isinstance(theme_options.get("icon_links", []), list):
        raise ExtensionError(
            "`icon_links` must be a list of dictionaries, you provided "
            f"type {type(theme_options.get('icon_links'))}."
        )

    # Set the anchor link default to be # if the user hasn't provided their own
    if not utils.config_provided_by_user(app, "html_permalinks_icon"):
        app.config.html_permalinks_icon = "#"

    # check the validity of the theme switcher file
    is_dict = isinstance(theme_options.get("switcher"), dict)
    should_test = theme_options.get("check_switcher", True)
    if is_dict and should_test:
        theme_switcher = theme_options.get("switcher")

        # raise an error if one of these compulsory keys is missing
        json_url = theme_switcher["json_url"]
        theme_switcher["version_match"]

        # try to read the json file. If it's a url we use request,
        # else we simply read the local file from the source directory
        # display a log warning if the file cannot be reached
        reading_error = None
        if urlparse(json_url).scheme in ["http", "https"]:
            try:
                request = requests.get(json_url)
                request.raise_for_status()
                content = request.text
            except (ConnectionError, HTTPError, RetryError) as e:
                reading_error = repr(e)
        else:
            try:
                content = Path(app.srcdir, json_url).read_text()
            except FileNotFoundError as e:
                reading_error = repr(e)

        if reading_error is not None:
            warning(
                f'The version switcher "{json_url}" file cannot be read due to '
                f"the following error:\n{reading_error}"
            )
        else:
            # check that the json file is not illformed,
            # throw a warning if the file is ill formed and an error if it's not json
            switcher_content = json.loads(content)
            missing_url = any(["url" not in e for e in switcher_content])
            missing_version = any(["version" not in e for e in switcher_content])
            if missing_url or missing_version:
                warning(
                    f'The version switcher "{json_url}" file is malformed; '
                    'at least one of the items is missing the "url" or "version" key'
                )

def setup(app):
    theme_dir = get_html_theme_path()
    app.add_html_theme("xyzstyle", str(theme_dir))
    app.connect("builder-inited", update_config)
    app.connect("html-page-context", update_context)
    template_path = get_html_template_path()
    app.config.templates_path.append(str(template_path))
    return {
        "version": __version_full__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
