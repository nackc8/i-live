#!/usr/bin/env python3

with open("test.txt") as file:
    print(file.read())
    print(f"Oj! Den var {len(file.read())} tecken lång")
