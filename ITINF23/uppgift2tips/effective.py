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
    conflict_resolution="resolve",
)

# Optioner som inte får anges tillsammans kan vara i en mutual-
# exclusiongrupp. Uppgiftsbeskrivningen säger att användaren bara
# får ange ett format, så t.ex. både --hash och --exclamation ska
# inte vara tillåtet.. (Däremot är det tillåtet att inte ange något
# format.)
#
# Se: https://docs.python.org/3/library/argparse.html#mutual-exclusion
#
filter_group = parser.add_mutually_exclusive_group()

for format in formats:
    filter_group.add_argument(
        format.short,
        format.long,
        # Se: https://docs.python.org/3/library/argparse.html#dest
        # Lagra värdet i variabeln "format". Om inget format anges
        # är den forsatt None. Om ett format anges så...
        dest="format",
        # Se: "store_const" i https://docs.python.org/3/library/argparse.html#action
        #     som beskriver både "store_const" och "const".
        # Lagra ett konstant värde om optionen väljs
        action="store_const",
        # Det konstanta värdet är Format-objektet.
        const=format,
        help=format.help,
    )

args = parser.parse_args()
