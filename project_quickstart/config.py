import re

from rich.console import Console

# Rich console instance
console = Console()

# Caching for the repos
CACHE_DIR = ".project_quickstart"

# CLI config for help
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

# Regex to match github URLs
GIT_URL_REGEX = re.compile(
    r"https?://(bitbucket|gitlab|github).com/(?P<username>[a-zA-Z0-9]+)/(?P<repository>[a-zA-Z0-9]+)"
)
