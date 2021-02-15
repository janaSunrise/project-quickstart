# -- Imports --
import os
import shutil
import sys
import time
from textwrap import dedent

import inquirer
import requests
from colorama import Fore, init as colorama_init
from git import Repo, exc

from project_quickstart.config import console
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
    readme_contents = dedent(f"""
    # {project_name}
    ### A project using the language {lang}
    """).strip()

    with console.status(f"{Fore.YELLOW}Initializing readme...", spinner="dots"):
        time.sleep(1)
        with open(os.path.join(project_path, "README.md"), 'w') as file:
            file.write(readme_contents)

    print(f"{Fore.GREEN}Initialized Readme.")


def create_source(lang: str, lang_extension: str, project_path: str) -> None:
    with console.status(f"{Fore.YELLOW}Initializing main{lang_extension}...", spinner="dots"):
        time.sleep(1)
        with open(os.path.join(project_path, f"main{lang_extension}"), 'w') as file:
            if hasattr(Languages, lang):
                file.write(getattr(Languages, lang))
            else:
                file.write("")

    print(f"{Fore.GREEN}Initialized main{lang_extension}.")


def create_gitignore(lang: str, project_path: str) -> bool:
    with console.status(f"{Fore.YELLOW}Creating .gitignore ...", spinner="dots"):
        time.sleep(1)

        req = requests.get(f"https://www.toptal.com/developers/gitignore/api/{lang}")

        if req.status_code != 200:
            print(f"{Fore.RED}Couldn't initialize gitignore due to Network Error!")
            return False

        gitignore_contents = req.text.strip()

        with open(os.path.join(project_path, ".gitignore"), 'w') as file:
            file.write(gitignore_contents)

        print(f"{Fore.GREEN}Initialized gitignore.")
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

    with console.status(f"{Fore.YELLOW}Creating license...", spinner="dots"):
        time.sleep(1)

        req = requests.get(f"https://api.github.com/licenses")

        if req.status_code != 200:
            print(f"{Fore.RED}Couldn't initialize gitignore due to Network Error!")
            return False

        license_url = req.json()[mapping[name]]["url"]

        req = requests.get(license_url)
        license_contents = req.json()["body"]

        with console.status(f"{Fore.YELLOW}Initializing License[{name}]", spinner="dots"):
            time.sleep(1)
            with open(os.path.join(project_path, "LICENSE"), 'w') as file:
                file.write(license_contents)

    print(f"{Fore.GREEN}Initialized license [{name}].")


def git_init(project_path: str) -> None:
    with console.status(f"{Fore.GREEN}Finalizing the project...", spinner="dots"):
        try:
            Repo.init(project_path)
        except exc.GitError as e:
            print(f"{Fore.RED} ERROR: {e!r}")
        except exc.GitCommandError as e:
            print(f"{Fore.RED} ERROR: {e!r}")

    print(f"{Fore.GREEN}Your project creation is finished.")


def remove_git_init(path: str) -> None:
    if not os.path.isdir(path) and os.path.exists(path):
        return

    shutil.rmtree(os.path.join(path, ".git"))
