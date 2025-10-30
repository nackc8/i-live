#!/usr/bin/env python3

Path

filename = "test.txt"

with open(filename) as file:
    content = file.readlines()
    print(content)
    print(f"Oj! Den var {len(content)} rader lång")
