import os
from .languages import languages

import sys
import requests
import time

from colorama import init, Fore

init(autoreset=True)

# Get the path to the project
project_path = input(f"{Fore.YELLOW}Enter the Path to your project Destination: ")

if not os.path.isdir(project_path) and os.path.exists(project_path):
    print(f"{Fore.RED}Invalid Path Entered!")
    sys.exit(-1)


# Get the Project name
project_name = input(f"{Fore.YELLOW}Enter the name for the project: ")

project_full_path = os.path.join(project_path, project_name)


# Create The Project
try:
    os.makedirs(project_full_path)
except OSError as error:
    print(error)
    sys.exit(-1)


# Get the data regarding the language being used in project
project_language = input(f"{Fore.CYAN}Enter the language to be used for the project: ")
project_lang_extension = input(f"{Fore.CYAN}Enter the extension for {project_language}: ")

if not project_lang_extension.startswith('.'):
    project_lang_extension = f".{project_lang_extension}"


# Create the README.md
print(f"{Fore.GREEN}Initializing readme...")

readme_contents = f"""
# {project_name}
### A project using the language {project_language}
"""

with open(os.path.join(project_full_path, "readme.md"), 'wb') as file:
    file.write(bytes(readme_contents.encode()))

time.sleep(1)


# Create the Gitignore
print(f"{Fore.GREEN}Creating .gitignore ...")

r = requests.get(f"https://www.toptal.com/developers/gitignore/api/{project_language}")

if r.status_code == 200:
    gitignore_contents = r.text.strip()
    with open(os.path.join(project_full_path, ".gitignore"), 'wb') as file:
        file.write(bytes(gitignore_contents.encode()))
else:
    print(f"{Fore.RED}Couldn't initalize gitignore due to Network Error!")


# Initialize the source
print(f"{Fore.GREEN}Initializing main.{project_lang_extension} ...")
with open(os.path.join(project_full_path, f"main.{project_lang_extension}"), 'wb') as file:
    if languages[project_language.lower()]:
        file.write(bytes(languages[project_language.lower()].encode()))
    else:
        file.write(bytes("".encode()))


# Git installed or not
answer = input("Is git installed on your system: ")[:1]

if answer == "n":
    print(f"{Fore.GREEN}The project is created")
    sys.exit(0)


# Execute git commands
output = os.popen(f'cd {project_full_path} && git init && git add . && git commit -m "initial commit"').read()
print(f"Output : {output}")
print(f"{Fore.GREEN}Your project creation is finished.")
