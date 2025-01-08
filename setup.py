import setuptools
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Classification-Deep-Learning-Project"
AUTHOR_USER_NAME = "Rahul2899"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "ramrajerahul2@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here, e.g.,
        "numpy>=1.19.2",
        "tensorflow>=2.5.0",
        "pandas>=1.1.3",
        "matplotlib>=3.3.2"
    ],
    python_requires=">=3.10",
)
