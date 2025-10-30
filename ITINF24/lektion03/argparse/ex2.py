#!/usr/bin/env python3

# stringmod ([-u|--uppercase] | [-l|--lowercase]) FILE
# Klart:         Ja          Nej     Ja           Ja

import argparse
import sys

parser = argparse.ArgumentParser(
    prog="stringmod",
    description="Modifies a text file and prints the result",
    epilog="Text at the bottom of help",
)

parser.add_argument("filename", help="The filename to read and transform")
parser.add_argument(
    "-l",
    "--lowercase",
    action="store_true",
    help="Transform the file contents to lowercase",
)
parser.add_argument(
    "-u",
    "--uppercase",
    action="store_true",
    help="Transform the file contents to uppercase",
)

if __name__ == "__main__":
    parser.parse_args()

# - Definiera argument och flaggor med `ArgumentParser()`

# - Ömsesidigt uteslutande grupper (`add_mutually_exclusive_group()`)

# - Booleska flaggor och positionella argument
