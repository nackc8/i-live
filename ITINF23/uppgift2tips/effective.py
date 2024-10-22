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
formats = [Format()]

"--hash", "-h"
"--dblslash", "-l"
"--dbldash", "-d"
"--percent", "-p"
"--apostrophe", "-a"
"--basic", "-b"
"--semicolon", "-s"
"--exclamation", "-e"
