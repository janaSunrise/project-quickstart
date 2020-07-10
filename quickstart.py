from os import path, mkdir, popen
import sys
import requests
import time


# Get the path to the project
project_path = input("Enter the Path to your project Destination: ")

if not path.isdir(project_path) and path.exists(project_path):
    print("Invalid Path Entered!")
    sys.exit(-1)


# Get the Project name
project_name = input("Enter the name for the project: ")

project_full_path = path.join(project_path, project_name)


# Create The Project
try:
    mkdir(project_full_path)
except OSError as error:
    print(error)
    sys.exit(-1)


# Get the data regarding the language being used in project
project_language = input("Enter the language to be used for the project: ")
project_lang_extension = input(f"Enter the extension for {project_language}: ")

if not project_lang_extension.startswith('.'):
    project_lang_extension = f".{project_lang_extension}"


# Create the README.md
print("Initializing readme...")

readme_contents = f"""
# {project_name}
### A project using the language {project_language}
"""

with open(path.join(project_full_path, "readme.md"), 'wb') as file:
    file.write(bytes(readme_contents.encode()))

time.sleep(1)


# Create the Gitignore
print("Creating .gitignore ...")

r = requests.get(f"https://www.toptal.com/developers/gitignore/api/{project_language}")

if r.status_code == 200:
    gitignore_contents = r.text.strip()
    with open(path.join(project_full_path, ".gitignore"), 'wb') as file:
        file.write(bytes(gitignore_contents.encode()))
else:
    print("Couldn't initalize gitignore due to Network Error!")


# Initialize the source
print(f"Initializing main.{project_lang_extension} ...")
with open(path.join(project_full_path, f"main.{project_lang_extension}"), 'wb') as file:
    file.write(bytes("".encode()))


# Git installed or not
answer = input("Is git installed on your system: ")[:1]

if answer == "n":
    print("The project is created")
    sys.exit(0)


# Execute git commands
output = popen('git init && git add . && git commit -m "initial commit"').read()
print(f"Output : {output}")
print("Your project creation is finished.")
