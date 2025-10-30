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

name=""
while name == ""
    name = input("What is your name? ")

me = {"name": name, "attack": 15, "health": 40, "sound": "hej!"}

animal = random.choice(animals)

print(f"You encounter a wild {animal['animal']}")
print(f"{animal["name"]}'s health is {me['health']}, its health is {animal['health']}")
print(f"{me["name"]}'s attack is {me['attack']}, the animals attack is {animal['attack']}")

while me["health"] > 0 and animal["health"] > 0:
    action = ""
    while not (action == "a" or action == "f"):
        action = input("Attack or flee (a/f)? ")

    if action == "a":
        success = True if random.randint(1, 100) > 50 else False
        if success:
            print(me["name"] + ": " + me["sound"])
            next_animal_health = animal["health"]
            next_animal_health -= me["attack"]
            animal["health"] = next_animal_health
            if animal["health"] > 0:
                print(
                    f"The {animal['animal']} is hit for {me['attack']}, it has {animal['health']} health left."
                )
            else:
                print(f"The {animal['animal']} is hit for {me['attack']}, it perished.")
                continue
        else:
            print(me["name"] + " missed!")

    animal_success = True if random.randint(1, 100) > 50 else False
    if animal_success:
        print(animal["sound"])
        next_me_health = me["health"]
        next_me_health -= animal["attack"]
        me["health"] = next_me_health
        if me["health"] > 0:
            print(
                f"You're hit for {animal['attack']}, you have {me['health']} health left."
            )
        else:
            print(f"The {animal['animal']} is hit for {me['attack']}, you are dead.")
            continue

    else:
        print(f"The {animal['animal']} missed!")

    if action == "f":
        success_flee = True if random.randint(1, 100) > 50 else False
        if success_flee:
            print("You cowardly ran away!")
            break

print("Game over")
