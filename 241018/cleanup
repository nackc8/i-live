#!/usr/bin/env python3

import argparse
import sys
import re

# # Mål: Byt ut repeterande specialtecken som :,.; och mellanslag mot endast ett tecken i
# en fil som användaren anger och skriv ut det till stdout.

# ln kod1.py cleanup # två namn, samma fil (funkar ivf i Linux)

parser = argparse.ArgumentParser(
    prog="cleanup",
    description="Cleans up a file by removing repetetive \
        special characters and writing the result to stdout.",
    epilog="Text at the bottom of help",
)

parser.add_argument("FILE")

args = parser.parse_args()

try:
    with open(args.FILE, encoding="utf-8") as f:
        file_lines = f.readlines()
except:
    print(f"{parser.prog}: error: the file does not exist or could not be read: FILE")
    sys.exit(3)

non_repeating_chars = ":,.; "


def repl(m):
    complete_match = m.group(0)
    used_char = complete_match[0]
    return used_char


repeating_regex_string = r":{2,}|,{2,}|[.]{2,}|;{2,}|[ ]{2,}"

repeating = re.compile(repeating_regex_string)

for line in enumerate(file_lines):
    file_lines[line[0]] = repeating.sub(repl, line[1])

output = "".join(file_lines)

# Skriv ut alla lines som en sträng

# Avsluta med en statuskod som betyder att det gick bra
