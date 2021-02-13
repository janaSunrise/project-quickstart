import re

# -- Cache config --
CACHE_DIR = ".project_quickstart"

# -- CLI config --
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

# -- Regex config --
GIT_URL_REGEX = re.compile(
    r'https?://(bitbucket|gitlab|github).com/(?P<username>[a-zA-Z0-9]+)/(?P<repository>[a-zA-Z0-9]+)'
)
