#!/usr/bin/env python3

import random


class Animal:
    def __init__(self, animal, attack, health, sound):
        self.animal = animal
        self.attack = attack
        self.health = health
        self.sound = sound


class Me:
    def __init__(self, name, attack, health, sound):
        self.name = name
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

name = ""
while name == "":
    name = input("What is your name? ")

me = Me(name, 15, 40, "hej!")

animal = random.choice(animals)

print(f"You encounter a wild {animal.animal}")
print(f"{me.name}'s health is {me.health} with attack {me.attack}")
print(f"The {animal.animal}'s health is {animal.health}, with attack {animal.attack}")

tried_to_flee = False
while me.health > 0 and animal.health > 0:
    if not tried_to_flee:
        action = ""
        while not (action == "a" or action == "f"):
            action = input("Attack or flee (a/f)? ")

        if action.lower() == "a":
            success = True if random.randint(1, 100) > 50 else False
            if success:
                print(me.name + ": " + me.sound)
                next_animal_health = animal.health
                next_animal_health -= me.attack
                animal.health = next_animal_health
                if animal.health > 0:
                    print(
                        f"The {animal.animal} is hit for {me.attack}, it has {animal.health} health left."
                    )
                else:
                    print(f"The {animal.animal} is hit for {me.attack}, it perished.")
                    continue
            else:
                print(me.name + " missed!")

    animal_success = True if random.randint(1, 100) > 50 else False
    if animal_success:
        print(animal.animal + ": " + animal.sound)
        next_me_health = me.health
        next_me_health -= animal.attack
        me.health = next_me_health
        if me.health > 0:
            print(f"You're hit for {animal.attack}, you have {me.health} health left.")
        else:
            print(f"The {animal.animal} is hit for {me.attack}, you are dead.")
            continue
    else:
        print(f"The {animal.animal} missed!")

    if not tried_to_flee and action.lower() == "f":
        tried_to_flee = True
        success_flee = True if random.randint(1, 100) > 50 else False
        if success_flee:
            print(f"{me.name} cowardly ran away!")
            break
    tried_to_flee = False

print("Game over")
