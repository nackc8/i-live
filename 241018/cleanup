#!/usr/bin/env python3

import argparse
import sys

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
print(args.FILE)

try:
    with open(args.FILE, encoding="utf-8") as f:
        file_lines = f.readlines()
except:
    print(f"{parser.prog}: error: the file does not exist or could not be read: FILE")
    sys.exit(3)


print(file_lines)
print(type(file_lines))


non_repeating_chars = ":,.; "


def repl(m):
    inner_word = list(m.group(2))
    random.shuffle(inner_word)
    return m.group(1) + "".join(inner_word) + m.group(3)


repeating_regex_string = r":{2,}|,{2,}|[.]{2,}|;{2,}|[ ]{2,}"

repeating = re.compile(repeating_regex_string)

# för varje line i file_lines
for line in enumerate(file_lines):
    print(f"rad: {line}", end="")

    line[line[0]] = repeating.sub(repl, line[1])

#    parts = en lista av de delar inom line där non_repeating_chars repeteras

#    för varje part i parts
#       line =
#         - Den nuvarande line, fast med delen part utbytt mot ett tecken.
#         - Det tecknet kan tas från första positionen i part.

# Notering: nu har vi en lines där radernas repeterande
#           non_repeating_chars-tecken bytts ut mot endast ett

# Skriv ut alla lines som en sträng

# Avsluta med en statuskod som betyder att det gick bra
