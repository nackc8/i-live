#!/usr/bin/env python3

import argparse

# # Mål: Byt ut repeterande specialtecken som :,.; och mellanslag mot endast ett tecken i
# en fil som användaren anger och skriv ut det till stdout.

# ln kod1.py kod # två namn, samma fil (funkar ivf i Linux)

parser = argparse.ArgumentParser(
    prog="cleanup",
    description="Cleans up a file by removing repetetive special characters and writing the result to stdout.",
    epilog="Text at the bottom of help",
)

parser.add_argument("FILE")

args = parser.parse_args()
print(args.FILE)

# om filen args.FILE inte finns eller inte kan läsas
#    skriv ett felmeddelande till stderr
#    avsluta med en statuskod som betyder att det blev fel

with open(args.FILE, encoding="utf-8") as f:
    read_data = f.read()

print(read_data)
print(type(read_data))

# if filen args.FILE inte finns eller inte kan läsas
#    skriv ett felmeddelande till stderr
#    avsluta med en statuskod som betyder att det blev fel

# file_lines = läs in alla rader i filen "args.FILE" till en lista med strängar

# non_repeating_chars = ":,.; "

# för varje line i file_lines
#    parts = en lista av de delar inom line där non_repeating_chars repeteras
#    för varje part i parts
#       line =
#         - Den nuvarande line, fast med delen part utbytt mot ett tecken.
#         - Det tecknet kan tas från första positionen i part.

# Notering: nu har vi en lines där radernas repeterande
#           non_repeating_chars-tecken bytts ut mot endast ett

# Skriv ut alla lines som en sträng

# Avsluta med en statuskod som betyder att det gick bra
