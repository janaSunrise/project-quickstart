import os
import time

import inquirer
from colorama import Fore, init as colorama_init

from project_quickstart.utils import (
    create_gitignore,
    create_license,
    create_readme,
    create_source,
    get_project_path,
    git_init,
    make_project_dirs,
)

colorama_init(autoreset=True)


def create_project() -> None:
    # -- Get project path and ensure it's existence --
    project_path = get_project_path()
    project_name = inquirer.text(message=f"{Fore.YELLOW}Enter the name for the project")

    project_full_path = os.path.join(project_path, project_name)
    make_project_dirs(project_full_path)

    # Get project language
    lang = inquirer.text(message=f"{Fore.CYAN}Enter the language to be used for the project").lower()

    lang_extension = inquirer.text(message=f"{Fore.CYAN}Enter the extension for {lang}").lower()

    if not lang_extension.startswith('.'):
        lang_extension = f".{lang_extension}"

    # -- Create the README.md --
    create_readme(project_name, lang, project_full_path)
    time.sleep(1)

    # -- Create License --
    license_choice = inquirer.list_input(
        "Which license do you want to use for your project?",
        choices=[
            "GNU Affero General Public License v3.0",
            "Apache License 2.0",
            "BSD 2-Clause \"Simplified\" License",
            "BSD 3-Clause \"New\" or \"Revised\" License",
            "GNU General Public License v2.0",
            "GNU General Public License v3.0",
            "GNU Lesser General Public License v2.1",
            "MIT License",
            "Mozilla Public License 2.0",
            "The Unlicense"
        ]
    )

    create_license(license_choice, project_full_path)
    time.sleep(1)

    # -- Initialize the source --
    create_source(lang, lang_extension, project_full_path)

    # -- Handle GIT --
    use_git = inquirer.confirm("Do you want to use git?")

    if not use_git:
        print(f"{Fore.GREEN}The project is created")
        return

    # -- Do the git file processing
    create_gitignore(lang, project_full_path)
    git_init(project_full_path)
