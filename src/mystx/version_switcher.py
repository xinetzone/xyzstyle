import os
from typing import Tuple, Optional
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util.typing import ExtensionMetadata

def configure_version_switcher(
    release: str = "mystx",  # Default to the current release version
    default_json_url: str = "https://xinetzone.github.io/mystx/_static/switcher.json",
    dev_json_url: str = "_static/switcher.json"
) -> tuple[str, str]:
    """Configure the version switcher settings based on the environment and release version.
    
    Args:
        release: The current release version string
        default_json_url: Default URL for the version switcher JSON file
        dev_json_url: URL to use for development versions
        
    Returns:
        A tuple containing (json_url, version_match)
        
    Raises:
        ValueError: If the release string is empty
    """
    if not release:
        raise ValueError("Release version cannot be empty")
    
    # Get the version from the environment or default to None
    version_match = os.environ.get("READTHEDOCS_VERSION")
    json_url = default_json_url
    
    # Determine which version to use based on environment or release string
    if not version_match or version_match.isdigit() or version_match == "latest":
        # For local development, infer the version from the package
        if any(marker in release for marker in ("dev", "rc")):
            version_match = "dev"
            json_url = dev_json_url
        else:
            version_match = f"v{release}"
    elif version_match == "stable":
        version_match = f"v{release}"
    
    return json_url, version_match


def sphinx_setup(app: Sphinx, config: Config) -> ExtensionMetadata:
    # Use the configure_version_switcher function to get json_url and version_match
    json_url, version_match = configure_version_switcher(
        # release=app.config.release,
        # project_name=app.config.project
    )
    config["html_theme_options"].update({"switcher": {
            "json_url": json_url,
            "version_match": version_match,
        },
        "primary_sidebar_end": ["version-switcher"],
    })
    # -- To demonstrate ReadTheDocs switcher -------------------------------------
    # This links a few JS and CSS files that mimic the environment that RTD uses
    # so that we can test RTD-like behavior. We don't need to run it on RTD and we
    # don't wanted it loaded in GitHub Actions because it messes up the lighthouse
    # results.
    if not os.environ.get("READTHEDOCS") and not os.environ.get("GITHUB_ACTIONS"):
        app.add_css_file(
            "https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css"
        )
        app.add_css_file("https://assets.readthedocs.org/static/css/badge_only.css")

        # Create the dummy data file so we can link it
        # ref: https://github.com/readthedocs/readthedocs.org/blob/bc3e147770e5740314a8e8c33fec5d111c850498/readthedocs/core/static-src/core/js/doc-embed/footer.js  # noqa: E501
        app.add_js_file("rtd-data.js")
        app.add_js_file(
            "https://assets.readthedocs.org/static/javascript/readthedocs-doc-embed.js",
            priority=501,
        )
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

# def setup(app):
#     # -- To demonstrate ReadTheDocs switcher -------------------------------------
#     # This links a few JS and CSS files that mimic the environment that RTD uses
#     # so that we can test RTD-like behavior. We don't need to run it on RTD and we
#     # don't wanted it loaded in GitHub Actions because it messes up the lighthouse
#     # results.
#     if not os.environ.get("READTHEDOCS") and not os.environ.get("GITHUB_ACTIONS"):
#         app.add_css_file(
#             "https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css"
#         )
#         app.add_css_file("https://assets.readthedocs.org/static/css/badge_only.css")

#         # Create the dummy data file so we can link it
#         # ref: https://github.com/readthedocs/readthedocs.org/blob/bc3e147770e5740314a8e8c33fec5d111c850498/readthedocs/core/static-src/core/js/doc-embed/footer.js  # noqa: E501
#         app.add_js_file("rtd-data.js")
#         app.add_js_file(
#             "https://assets.readthedocs.org/static/javascript/readthedocs-doc-embed.js",
#             priority=501,
#         )
