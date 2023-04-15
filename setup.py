"""Builds the package.
@author: Younggue Bae
"""
import os
import sys
import pkg_resources
from setuptools import setup, find_packages


VERSION = "0.0.0"
DESCRIPTION = "next-diffusion"

setup(
    name="next-diffusion",
    version=VERSION,
    description=DESCRIPTION,
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Younggue Bae",
    # author_email="<louiezzang@gmail.com>",
    package_dir={"": "src"},
    url="https://github.com/louiezzang/next-diffusion",
    keywors=[
        "Diffusers",
        "Diffusion",
    ],
    packages=find_packages(where="src"),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    python_requires=">=3.6",
    include_package_data=True,
)
