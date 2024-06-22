#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages


requirements = ["Click>=7.0", "gotify", "platformdirs"]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Hendrik Klug",
    author_email="hendrik.klug@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Command line interface for gotify",
    entry_points={
        "console_scripts": [
            "gotify_cli=gotify_cli.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords="gotify_cli",
    name="gotify_cli",
    packages=find_packages(include=["gotify_cli", "gotify_cli.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/Jimmy2027/gotify_cli",
    version="0.1.0",
    zip_safe=False,
)
