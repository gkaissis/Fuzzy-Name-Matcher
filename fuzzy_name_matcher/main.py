#! /usr/bin/python

import os
import sys
from pathlib import Path
from typing import List, Tuple, Union

import pandas as pd
from fuzzywuzzy import process
from tqdm import tqdm

os.chdir(os.path.dirname(sys.argv[0]))


def main():

    output_dict = dict()

    excel_file = input(
        "Please specify the path to the Excel File. A column 'Full Name' must be present. "
    )
    directory = input(
        "Please specify the path to the top-level directory containing the folders to check. "
    )

    input_names: List = get_full_name_column(excel_file)
    candidate_names = [folder for folder in get_folder_paths_and_names(directory)]

    print("Processing...")
    for name in tqdm(input_names):
        (found_name, score), found = match_names_and_folders(name, candidate_names)
        output_dict[name] = [found_name, score, found]

    output_df = pd.DataFrame.from_dict(
        output_dict, columns=["Path", "Score", "Found"], orient="index"
    )
    print("Writing Excel file...")
    output_excel(output_df)
    print(f"Done! Results file can be found at {os.getcwd()}")
    sys.exit(0)


def get_full_name_column(excel_file: Path) -> List[str]:
    """
    Gets the "Full Name" column from an Excel file.

    Arguments:
    excel_file: str or pathlike, path to the excel file

    Returns:
    List of names found in the Full Name column

    Raises:
    RuntimeError if the excel file has no "Full Name" column.
    """

    path_to_file = Path(excel_file).resolve()
    f = pd.read_excel(path_to_file)
    if not "Full Name" in f.columns:
        raise RuntimeError("""Excel File must have a column 'Full Name'.""")
    return f["Full Name"].tolist()


def get_folder_paths_and_names(path_to_parent_dir: Path) -> List[Path]:
    """
    Gets the paths and names of the folders in a directory.

    Arguments:
    path_to_parent_dir: str or pathlike, path to the parent directory

    Returns:
    Tuple of lists with the paths to the subfolders and the names of the subfolders

    Raises:
    None
    """
    path_to_iterate = Path(path_to_parent_dir).resolve()
    return [folder for folder in path_to_iterate.iterdir() if folder.is_dir()]


def match_names_and_folders(
    name: str, folder_list: List[str]
) -> Union[Tuple[Tuple[str, int]], Tuple[Tuple[str, None], int]]:
    """
    Matches a name with an entry in the folder list. Returns the most likely match and the score.

    Arguments:
    name: str, the name to check for
    folder_list: list, the list of names to check against

    Returns:
    Tuple of the name which was found and the score

    Raises:
    None
    """
    result = process.extractOne(query=name, choices=folder_list, score_cutoff=90)
    if result:
        return (result, 1)
    return ((f"Not found", None), 0)


def output_excel(df: pd.DataFrame) -> None:
    df.to_excel("Result.xlsx")  # type: ignore


if __name__ == "__main__":
    main()
