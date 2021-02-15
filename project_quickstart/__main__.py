#!/usr/bin/env python3
import os
import time
from textwrap import dedent

import inquirer
from click import Path, argument, group, option
from colorama import Fore, Style, init as colorama_init
from git import Repo, exc
from rich import print as rprint
from rich.console import RenderGroup
from rich.panel import Panel

from project_quickstart.utils import (
    create_gitignore,
    create_license,
    create_readme,
    create_source,
    get_project_path,
    git_init,
    make_project_dirs,
    remove_git_init
)
from project_quickstart.config import console, CACHE_DIR, CONTEXT_SETTINGS, GIT_URL_REGEX

# -- Config --
colorama_init(autoreset=True)


@group(context_settings=CONTEXT_SETTINGS)
def main() -> None:
    """
    This is a utility CLI program, that helps you get started with your projects by generating them quick from scratch,
    just clone your favorite repo, or use a repository as the template base.
    """
    pass


@main.command()
@option("-l", "--license", is_flag=True, help="Get a license from the library added to your project.")
@option("-g", "--git", is_flag=True, help="Adding the project to git for quick deploying and getting started with repo")
def init(license: bool, git: bool) -> None:
    """Get started with your ideas without spending any time on creating the projects."""
    project_path = get_project_path()
    project_name = inquirer.text(message=f"{Style.BRIGHT}{Fore.YELLOW}Enter the name for the project")

    # -- Create the project folders --
    project_full_path = os.path.join(project_path, project_name)
    make_project_dirs(project_full_path)

    # -- Get project language --
    lang = inquirer.text(message=f"{Style.BRIGHT}{Fore.CYAN}Enter the language to be used for the project").lower()
    lang_extension = inquirer.text(message=f"{Style.BRIGHT}{Fore.CYAN}Enter the extension for {lang}").lower()

    if not lang_extension.startswith('.'):
        lang_extension = f".{lang_extension}"

    # -- Create the README.md --
    create_readme(project_name, lang, project_full_path)
    time.sleep(1)

    # -- Create License --
    if license:
        license_choice = inquirer.list_input(
            f"{Style.BRIGHT}{Fore.GREEN}Which license do you want to use for your project?",
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
    if not git:
        print(f"{Style.BRIGHT}{Fore.GREEN}The project is created")

        panel_group = RenderGroup(
            Panel("Summary", style="bold cyan"),
            Panel(dedent(f"""
                Project name: {project_name}
                Project path: {project_full_path}

                Language: {lang}

                ✓ Source files
                ✓ Readme
                {"✗" if not license else "✓"} License
                {"✗" if not git else "✓"} Initialized git and gitignore.

                Have an awesome day!
                """), style="bold cyan")
        )
        rprint(Panel(panel_group))

        return

    # -- Do the git file processing
    create_gitignore(lang, project_full_path)
    git_init(project_full_path)

    panel_group = RenderGroup(
        Panel("Summary", style="bold cyan"),
        Panel(dedent(f"""
        Project name: {project_name}
        Project path: {project_full_path}

        Language: {lang}

        ✓ Source files
        ✓ Readme
        {"✗" if not license else "✓"} License
        {"✗" if not git else "✓"} Initialized git and gitignore.

        Have an awesome day!
        """), style="bold cyan")
    )
    rprint(Panel(panel_group))


@main.command()
@argument("repository")
@argument("location", type=Path(exists=True))
@option("-c", "--cache", is_flag=True, help="If you need to cache the repo.")
def template(repository, location, cache) -> None:
    """Initialize the project with a template from a git repository into a specific location."""
    git_url_check = GIT_URL_REGEX.match(repository)

    home = os.path.expanduser("~")
    cache_path = os.path.join(home, CACHE_DIR)

    if location == ".":
        location = "./" + git_url_check.group("repository")

    if not git_url_check:
        print(f"{Style.BRIGHT}{Fore.RED}The URL for the repository is invalid!")
        return

    try:
        with console.status(f"{Style.BRIGHT}{Fore.YELLOW}Cloning the repo...", spinner="dots"):
            Repo.clone_from(repository, location)

        print(f"{Style.BRIGHT}{Fore.GREEN}Cloned the repo.")

        with console.status(f"{Style.BRIGHT}{Fore.YELLOW}Finalizing the project...", spinner="dots"):
            remove_git_init(location)

        print(f"{Style.BRIGHT}{Fore.GREEN}Removed git config.")

        if cache:
            with console.status(f"{Style.BRIGHT}{Fore.YELLOW}Caching the template..", spinner="dots"):
                Repo.clone_from(repository, cache_path)

            print(f"{Style.BRIGHT}{Fore.GREEN}Successfully cached the repo.")
    except exc.GitError as e:
        print(f"{Style.BRIGHT}{Fore.RED} ERROR: {e!r}")
    except exc.GitCommandError as e:
        print(f"{Style.BRIGHT}{Fore.RED} ERROR: {e!r}")

    print(f"{Style.BRIGHT}{Fore.GREEN}Your template creation is finished.")

    panel_group = RenderGroup(
        Panel("Summary", style="bold cyan"),
        Panel(dedent(f"""
            Repository: {repository}
            Template location: {location}

            ✓ Template downloaded
            {"✗" if not cache else "✓"} Cached ({cache_path + git_url_check.group("repository")})

            Have an awesome day!
            """), style="bold cyan")
    )
    rprint(Panel(panel_group))
