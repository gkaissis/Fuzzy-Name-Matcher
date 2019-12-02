# Fuzzy Name Matcher

## Description

This module searches an Excel file for a column named "Full Name", then searches a directory with subfolders with fuzzy matching and returns an Excel File with the folders it found, the confidence that they are identical and whether they were found in the directory.

## Installation

**Please note that this software is incompatible with Python 2**

1. Create a new virtual environment
2. Run `pip install git+https://github.com/gkaissis/Fuzzy-Name-Matcher`
3. Run `python fuzzy.py`

## Usage

The software will prompt for the path to an Excel file with the column "Full Name" and for the path to a folder. Please don't put quotes around the paths. After the progress bar has finished, it will return an Excel file in the current directory.

## Contributing

Contributions are welcome via PR. Please note that:

1. Typed Python is used throughout the project. We recommend installing `mypy` for type checking and linting.
2. We require adherence to `PEP8`. Please use `black` as your formatter.
