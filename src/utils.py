import requests


def get_gitignore(language):
    r = requests.get(f"https://www.toptal.com/developers/gitignore/api/{project_language}")

    if r.status_code == 200:
        gitignore_contents = r.text.strip()
        return gitignore_contents
    
    else:
        return None
