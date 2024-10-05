"""Here are some utility functions for reading input data and displaying the results."""


import os
from pprint import pprint
from re import Match, search


def compact(args, w=100):
    pprint(args, depth=2, compact=True, width=w)


def read_data(filename: str) -> list[str]:
    data: list[str] = []
    input_files: list[str] = []
    current_filename: str = os.path.basename(filename).split('.')[0]

    for root, _, filenames in os.walk(os.getcwd()):
        for filename in filenames:
            if filename.endswith(".txt"):
                input_files.append(os.path.join(root, filename))

    for input_file in input_files:
        result: Match[str] | None = search(current_filename, input_file)
        if result:
            with open(input_file, "r") as f:
                data = f.read().strip().split("\n")

    return data


if __name__ == "__main__":
    print("Hello friend.")
