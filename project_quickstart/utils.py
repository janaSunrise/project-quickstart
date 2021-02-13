# -- Imports --
import os
import sys
from textwrap import dedent

import inquirer
import requests
from colorama import Fore, init as colorama_init

from project_quickstart.languages import Languages

colorama_init(autoreset=True)


# -- Utility functions --
def get_project_path() -> str:
    path = inquirer.text(message=f"{Fore.YELLOW}Enter the path to your project destination")

    if not os.path.isdir(path) and os.path.exists(path):
        print(f"{Fore.RED}Invalid Path Entered!")
        sys.exit(-1)

    return path


def make_project_dirs(project_full_path: str) -> None:
    try:
        os.makedirs(project_full_path)
    except OSError as exc:
        print(exc)
        sys.exit(-1)


def create_readme(project_name: str, lang: str, project_path: str) -> None:
    print(f"{Fore.GREEN}Initializing readme...")

    readme_contents = dedent(f"""
    # {project_name}
    ### A project using the language {lang}
    """)

    with open(os.path.join(project_path, "README.md"), 'w') as file:
        file.write(readme_contents)


def create_source(lang: str, lang_extension: str, project_path: str) -> None:
    print(f"{Fore.GREEN}Initializing main{lang_extension} ...")

    with open(os.path.join(project_path, f"main{lang_extension}"), 'w') as file:
        if hasattr(Languages, lang):
            file.write(getattr(Languages, lang))
        else:
            file.write("")


def create_gitignore(lang: str, project_path: str) -> bool:
    print(f"{Fore.GREEN}Creating .gitignore ...")

    r = requests.get(f"https://www.toptal.com/developers/gitignore/api/{lang}")

    if r.status_code != 200:
        print(f"{Fore.RED}Couldn't initialize gitignore due to Network Error!")
        return False

    gitignore_contents = r.text.strip()

    with open(os.path.join(project_path, ".gitignore"), 'w') as file:
        file.write(gitignore_contents)

    return True


def create_license(name: str, project_path: str) -> bool:
    mapping = {
        "GNU Affero General Public License v3.0": 0,
        "Apache License 2.0": 1,
        "BSD 2-Clause \"Simplified\" License": 2,
        "BSD 3-Clause \"New\" or \"Revised\" License": 3,
        "GNU General Public License v2.0": 7,
        "GNU General Public License v3.0": 8,
        "GNU Lesser General Public License v2.1": 9,
        "MIT License": 10,
        "Mozilla Public License 2.0": 11,
        "The Unlicense": 12
    }

    req = requests.get(f"https://api.github.com/licenses")

    if req.status_code != 200:
        print(f"{Fore.RED}Couldn't initialize gitignore due to Network Error!")
        return False

    license_url = req.json()[mapping[name]]["url"]

    req = requests.get(license_url)
    license_contents = req.json()["body"]

    print(f"{Fore.GREEN}Initializing LICENSE [{name}]")

    with open(os.path.join(project_path, "LICENSE"), 'w') as file:
        file.write(license_contents)


def git_init(project_path: str) -> None:
    output = os.popen(f'cd {project_path} && git init && git add . && git commit -m "initial commit"').read()
    print(f"Output: {output}")
    print(f"{Fore.GREEN}Your project creation is finished.")
