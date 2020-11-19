import os
import sys
import time

import requests
from colorama import Fore, init as colorama_init

from src.languages import languages

colorama_init(autoreset=True)


def get_project_path() -> str:
    path = input(f"{Fore.YELLOW}Enter the path to your project destination: ")

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


def main() -> None:
    # Get project path and ensure it's existence
    project_path = get_project_path()
    project_name = input(f"{Fore.YELLOW}Enter the name for the project: ")
    project_full_path = os.path.join(project_path, project_name)
    make_project_dirs(project_full_path)

    # Get project language
    lang = input(f"{Fore.CYAN}Enter the language to be used for the project: ").lower()
    lang_extension = input(f"{Fore.CYAN}Enter the extension for {lang}: ").lower()

    if not lang_extension.startswith('.'):
        lang_extension = f".{lang_extension}"

    # Create the README.md
    print(f"{Fore.GREEN}Initializing readme...")

    readme_contents = f"""
    # {project_name}
    ### A project using the language {lang}
    """

    with open(os.path.join(project_full_path, "readme.md"), 'w') as file:
        file.write(readme_contents)

    time.sleep(1)

    # Create the gitignore
    print(f"{Fore.GREEN}Creating .gitignore ...")

    r = requests.get(f"https://www.toptal.com/developers/gitignore/api/{lang}")
    if r.status_code == 200:
        gitignore_contents = r.text.strip()
        with open(os.path.join(project_full_path, ".gitignore"), 'w') as file:
            file.write(gitignore_contents)
    else:
        print(f"{Fore.RED}Couldn't initialize gitignore due to Network Error!")

    # Initialize the source
    print(f"{Fore.GREEN}Initializing main{lang_extension} ...")

    with open(os.path.join(project_full_path, f"main.{lang_extension}"), 'w') as file:
        if languages.get(lang):
            file.write(languages[lang])
        else:
            file.write("")

    # Handle GIT
    answer = input("Do you want to use git? (Y/n): ").lower()[:1]

    if answer == "n":
        print(f"{Fore.GREEN}The project is created")
        return

    output = os.popen(
        f'cd {project_full_path} && git init && git add . && git commit -m "initial commit"'
    ).read()
    print(f"Output: {output}")
    print(f"{Fore.GREEN}Your project creation is finished.")


if __name__ == "__main__":
    main()
