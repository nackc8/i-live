#!/usr/bin/env python3

with open("test.txt") as file:
    content = file.readlines()
    print(content)
    print(f"Oj! Den var {len(content)} rader lång")
