#!/usr/bin/env python3

with open("test.txt") as file:
    content = file.read()
    print(content)
    print(f"Oj! Den var {len(content)} tecken lång")
