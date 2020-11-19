import os
import time

import inquirer
from colorama import Fore, init as colorama_init

from src.utils import (
    create_gitignore,
    create_readme,
    create_source,
    get_project_path,
    git_init,
    make_project_dirs,
)

colorama_init(autoreset=True)


def main() -> None:
    # Get project path and ensure it's existence
    project_path = get_project_path()
    project_name = inquirer.text(message=f"{Fore.YELLOW}Enter the name for the project")
    project_full_path = os.path.join(project_path, project_name)
    make_project_dirs(project_full_path)

    # Get project language
    lang = inquirer.text(
        message=f"{Fore.CYAN}Enter the language to be used for the project"
    ).lower()

    lang_extension = inquirer.text(
        message=f"{Fore.CYAN}Enter the extension for {lang}"
    ).lower()

    if not lang_extension.startswith('.'):
        lang_extension = f".{lang_extension}"

    # Create the README.md
    create_readme(project_name, lang, project_full_path)
    time.sleep(1)

    # Initialize the source
    create_source(lang, lang_extension, project_full_path)

    # Handle GIT
    use_git = inquirer.confirm("Do you want to use git?")

    if not use_git:
        print(f"{Fore.GREEN}The project is created")
        return

    create_gitignore(lang, project_full_path)
    git_init(project_full_path)


if __name__ == "__main__":
    main()
