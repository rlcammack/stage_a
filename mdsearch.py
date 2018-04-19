
"""Tool for finding markdown files within a directory.

This module can be used to quickly find markdown files withing a specified directory.

Command line usage:
mdedit.py [-h] [--verbose] [--file FILE] directory

Options:

positional arguments:
  directory             The directory to be searched

optional arguments:
  -h, --help            show this help message and exit
  --verbose, -v         Print complete file path
  --file FILE, -f FILE  Search for a specific file
"""

import argparse
import os
from csc440_robby_stage_a import stage_a_search


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="The directory to be searched")
    parser.add_argument("--verbose", "-v", help="Print complete file path", action="store_true")
    parser.add_argument("--file", "-f", help="Search for a specific file")

    args = parser.parse_args()
    my_search = stage_a_search.Search(os.listdir(args.directory))

    if args.file:
        for file in my_search.search_area:
            if file == args.file:
                    print(file)
    else:
        for file in my_search.search_area:
            if file.endswith(".md"):
                if args.verbose:
                    print(os.path.join(args.directory, file))
                else:
                    print(file)
