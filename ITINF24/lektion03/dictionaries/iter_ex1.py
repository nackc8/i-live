#!/usr/bin/env python3

import random

# Animal       Attack       Health      Sound
# donkey       20           80          "Ihhohhh"
# giraffe      40           50          "..."
# monkey       60           40          "Oh oh ah ah"
# pinguin      10           10          "Meek! Meek!"
# armadillo    5            100         "Piiiiip!"

animals = [
    {"animal": "donkey", "attack": 20, "health": 80, "sound": "Ihhohhh"},
    {"animal": "giraffe", "attack": 40, "health": 50, "sound": "..."},
    {"animal": "monkey", "attack": 60, "health": 40, "sound": "Oh oh ah ah"},
    {"animal": "pinguin", "attack": 10, "health": 10, "sound": "Meek! Meek!"},
    {"animal": "armadillo", "attack": 5, "health": 100, "sound": "Piiiiip!"},
]

me = {"attack": 15, "health": 40, "sound": "hej!"}

animal = random.choice(animals)

while me["health"] > 0 and animal["health"] > 0:
    # TODO: Info innan
    print(f"You encounter a wild {animal['animal']}")

    action = ""
    while not (action == "a" or action == "f"):
        action = input("Attack or flee (a/f)? ")

    print(me)
    print(animal)
    break
