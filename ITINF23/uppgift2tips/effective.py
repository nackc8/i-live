#!/usr/bin/env python3

# Om vi har följande tabell för formaten (jag har korrigerat ett fel jag
# gjorde i den, men det är inte viktigt)
#
# | Long^1          | Short^2 | Indicator^3     | Används i                  |
# | --------------- | ------- | --------------- | -------------------------- |
# | `--hash`        | `-h`    | `#`             | [Bash][1], [Python][2]     |
# | `--dblslash`    | `-l`    | `//`            | [C][3], [Java][4]          |
# | `--dbldash`     | `-d`    | `--`            | [SQL][5], [Lua][6]         |
# | `--percent`     | `-p`    | `%`             | [LaTeX][7], [MATLAB][8]    |
# | `--apostrophe`  | `-a`    | `'`             | [Visual Basic][9]          |
# | `--basic`       | `-b`    | `REM` eller `'` | [BASIC][10]                |
# | `--semicolon`   | `-s`    | `;`             | [Lisp][11], [Assembly][12] |
# | `--exclamation` | `-e`    | `!`             | [Fortran][13]              |


# Ett sätt att representera en rad i tabellen kan vara med en klass:

import re
import argparse


class Format:
    def __init__(self, long, short, indicator, help):
        self.long = long
        self.short = short
        # Vi gör om "indikatorn" (som # eller //) till ett reguljärt uttryck
        # som säger: början på raden kan inledas med vita tecken, sedan
        # kommer indikatorn. Då har vi ett regex-objekt som vi kan använda
        # för att matcha rader.
        self.indicator = re.compile(f"^\s*{indicator}")
        self.help = help


# Lägg alla formaten i listan med format. Varje rad är en instans av Format.
formats = [
    Format("--hash", "-h", "#", "Filters hash comments."),
    Format("--dblslash", "-l", "//", "Filters double slash comments."),
    Format("--dbldash", "-d", "--", "Filters double dash comments."),
    # Procenttecken behöver skrivas dubbelt då det är ett procenttecken
    # vill skriva. Det är en egenhet hos argparse.
    Format("--percent", "-p", "%%", "Filters percent comments."),
    Format("--apostrophe", "-a", "'", "Filters apostrophe comments."),
    Format("--basic", "-b", "REM|'", "Filters REM or apostrophe comments."),
    Format("--semicolon", "-s", ";", "Filters semicolon comments."),
    Format("--exclamation", "-e", "!", "Filters exclamation comments."),
]

parser = argparse.ArgumentParser(
    prog="effective",
    description="Removes comments and blank lines from files.",
)

parser.add_argument("FILE")

args = parser.parse_args()
