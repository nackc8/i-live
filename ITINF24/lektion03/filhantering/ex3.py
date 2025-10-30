#!/usr/bin/env python3

import sys
from pathlib import Path

# Vi använder en Path, for att kolla undersöka saker
filename = Path("testmissing.txt")

if not filename.exists():
    print(f"The file '{filename}' does not exist", file=sys.stderr)
    sys.exit(1)

with open(filename) as file:
    content = file.readlines()
    print(content)
    print(f"Oj! Den var {len(content)} rader lång")
