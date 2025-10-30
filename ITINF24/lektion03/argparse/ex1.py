#!/usr/bin/env python3

# stringmod ([-u|--uppercase] | [-l|--lowercase]) FILE

import argparse

parser = argparse.ArgumentParser(
    prog="stringmod",
    description="Modifies a text file and prints the result",
    epilog="Text at the bottom of help",
)

parser.add_argument("FILE",)

if __name__ == "__main__":
    parser.parse_args([])

# - Definiera argument och flaggor med `ArgumentParser()`

# - Ömsesidigt uteslutande grupper (`add_mutually_exclusive_group()`)

# - Booleska flaggor och positionella argument
