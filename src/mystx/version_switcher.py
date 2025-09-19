import os
from pathlib import Path
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util.typing import ExtensionMetadata
from sphinx.util import logging
logger = logging.getLogger(__name__)

def sphinx_setup(app: Sphinx, config: Config) -> ExtensionMetadata:
    logger.info("正在配置版本切换器")
    json_url = getattr(config, "version_switcher_json_url", "")
    release = config.release
    # Get the version from the environment or default to None
    version_match = os.environ.get("READTHEDOCS_VERSION")
    # Determine which version to use based on environment or release string
    if not version_match or version_match.isdigit() or version_match == "latest":
        # For local development, infer the version from the package
        if any(marker in release for marker in ("dev", "rc")):
            version_match = "dev"
            json_url = "_static/switcher.json" #str(Path(app.outdir)/"_static/switcher.json")
        else:
            version_match = f"v{release}"
    elif version_match == "stable":
        version_match = f"v{release}"
    logger.info(f"配置 version switcher: json_url={json_url}, version_match={version_match}")
    
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
