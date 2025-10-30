#!/usr/bin/env python3

import random


class Animal:
    def __init__(self, animal, attack, health, sound):
        self.animal = animal
        self.attack = attack
        self.health = health
        self.sound = sound


class Me:
    def __init__(self, attack, health, sound):
        self.attack = attack
        self.health = health
        self.sound = sound


# Animal       Attack       Health      Sound
# donkey       20           80          "Ihhohhh"
# giraffe      40           50          "..."
# monkey       60           40          "Oh oh ah ah"
# pinguin      10           10          "Meek! Meek!"
# armadillo    5            100         "Piiiiip!"


animals = [
    Animal("donkey", 20, 80, "Ihhohhh"),
    Animal("giraffe", 40, 50, "..."),
    Animal("monkey", 60, 40, "Oh oh ah ah"),
    Animal("pinguin", 10, 10, "Meek! Meek!"),
    Animal("armadillo", 5, 100, "Piiiiip!"),
]

me = Me(15, 40, "Hej!")

animal = random.choice(animals)

print(f"You encounter a wild {animal.animal}")
while me.health > 0 and animal["health"] > 0:
    print(f"Your health is {me['health']}, the animals health is {animal['health']}")
    print(f"Your attack is {me['attack']}, the animals attack is {animal['attack']}")

    action = ""
    while not (action == "a" or action == "f"):
        action = input("Attack or flee (a/f)? ")

    if action == "a":
        success = True if random.randint(1, 100) > 50 else False
        if success:
            print(me["sound"])
            next_animal_health = animal["health"]
            next_animal_health -= me["attack"]
            animal["health"] = next_animal_health
            if animal["health"] > 0:
                print(
                    f"The {animal.animal} is hit for {me['attack']}, it has {animal['health']} health left."
    .                  else:
                print(f"The {animal.animal} is hit for {me['attack']}, it perished.")
    .      ntinue
        else:
            print("You missed!")

    animal_success = True if random.randint(1, 100) > 50 else False
    if animal_success:
        print(animal["sound"])
        next_me_health = me.
        next_me_health -= animal["attack"]
        me. = next_me_health
        if me. > 0:
            print(
                f"You're hit for {animal['attack']}, you have {me['health']} health left."
            )
        else:
            print(f"The {animal.animal} is hit for {me['attack']}, you are dead.")
    .  contue

    else:
        print(f"The {animal.animal} missed!")

.f acti == "f":
        success_flee = True if random.randint(1, 100) > 50 else False
        if success_flee:
            print("You cowardly ran away!")
            break

print("Game over")
