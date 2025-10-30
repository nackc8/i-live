#!/usr/bin/env python3

from pathlib import Path

filename = Path("")

with open(filename) as file:
    content = file.readlines()
    print(content)
    print(f"Oj! Den var {len(content)} rader lång")
