from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.readme()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="read text from image with Python",
    version="0.0.1",
    author="Sabrina B. M.",
    author_email="sabrinabm94@gmail.com",
    description="package to extract a text file from image",
    long_description="",
    long_description_content_type="",
    url="https://github.com/sabrinabm94/python/tree/master/data-engineering/challenges/package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)
