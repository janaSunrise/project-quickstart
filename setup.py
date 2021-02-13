import re
from pathlib import Path

import setuptools

# Files
BASE_DIR = Path(__file__).resolve().parent

README = Path(BASE_DIR / "README.md").read_text()

# Constants
VERSION = re.search(
    r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
    Path(BASE_DIR / "project_quickstart/__init__.py").read_text(),
    re.MULTILINE
).group(1)

URL = "https://github.com/janaSunrise/project-quickstart"

if not VERSION:
    raise RuntimeError("VERSION is not set!")

# Setup
setuptools.setup(
    name="ProjectQuickstart",
    version=VERSION,

    author="Sunrit Jana",
    author_email="warriordefenderz@gmail.com",

    description="An easy way to create projects manually, or using templates!",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",

    url=URL,
    project_urls={
        "Documentation": URL,
        "Issue tracker": f"{URL}/issues",
    },

    packages=setuptools.find_packages(
        exclude=["tests", "tests.*", "tools", "tools.*"]
    ),
    entry_points={
        'console_scripts': [
            'project-quickstart = project_quickstart.__main__:main'
        ]
    },
    install_requires=[
        "requests==2.25.0",
        "colorama==0.4.4",
        "inquirer ==2.7.0",
        "click==7.1.2"
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",

        "Development Status :: 2 - Pre-Alpha",

        "Programming Language :: Python :: Implementation :: CPython",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",

        "Topic :: Scientific/Engineering :: Mathematics",

        "Natural Language :: English",
    ],

    python_requires='>=3.7',
)