import os
from typing import Tuple, Optional
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util.typing import ExtensionMetadata

def configure_version_switcher(
    release: str, 
    dev_json_url: str = "_static/switcher.json",
    project_name: Optional[str] = None,
    default_json_url: str = "https://pydata-sphinx-theme.readthedocs.io/en/latest/_static/switcher.json",
) -> Tuple[str, str]:
    """Configure the version switcher settings based on the environment and release version.
    
    Args:
        release: The current release version string
        default_json_url: Default URL for the version switcher JSON file
        dev_json_url: URL to use for development versions
        project_name: Optional project name to construct custom JSON URL
        
    Returns:
        A tuple containing (json_url, version_match)
        
    Raises:
        ValueError: If the release string is empty
    """
    if not release:
        raise ValueError("Release version cannot be empty")
    
    # Get the version from the environment or default to None
    version_match = os.environ.get("READTHEDOCS_VERSION")
    
    # If project name is provided, construct a custom JSON URL
    if project_name:
        # 清理项目名称，移除空格和其他可能导致URL无效的字符
        sanitized_project_name = project_name.replace(' ', '-').lower()
        # 如果项目名称包含中文字符或清理后为空，则使用默认URL
        if any('\u4e00' <= char <= '\u9fff' for char in sanitized_project_name) or not sanitized_project_name:
            json_url = default_json_url
        else:
            json_url = f"https://{sanitized_project_name}.readthedocs.io/zh-cn/latest/_static/switcher.json"
    else:
        json_url = default_json_url
    
    # Determine which version to use based on environment or release string
    if not version_match or version_match.isdigit() or version_match == "latest":
        # For local development, infer the version from the package
        if "dev" in release or "rc" in release:
            version_match = "dev"
            # We want to keep the relative reference if we are in dev mode
            # but we want the whole url if we are effectively in a released version
            json_url = dev_json_url
        else:
            version_match = f"v{release}"
    elif version_match == "stable":
        version_match = f"v{release}"
    
    return json_url, version_match

def sphinx_setup(app: Sphinx, config: Config) -> ExtensionMetadata:
    # Use the configure_version_switcher function to get json_url and version_match
    json_url, version_match = configure_version_switcher(
        release=app.config.release,
        project_name=app.config.project
    )
    footer_start = config["html_theme_options"].get("footer_start", [])
    if "version-switcher" not in footer_start:
        footer_start.append("version-switcher")
    config["html_theme_options"].update({"switcher": {
            "json_url": json_url,
            "version_match": version_match,
        },
        "footer_start": footer_start,
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
