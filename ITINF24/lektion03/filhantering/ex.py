#!/usr/bin/env python3

with open("test.txt") as file:
    content: str | list[str] = file.read()
    content = content.splitlines()
    print(content)
    print(f"Oj! Den var {len(content)} tecken lång")
