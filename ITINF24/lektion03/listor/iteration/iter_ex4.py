#!/usr/bin/env python3

animals = ["donkey", "giraffe", "monkey", "pinguin", "armadillo"]

good_animals = []
for animal in animals:
    good_animals.append(animal * 2)

# good_animals = [animal * 2 for animal in animals]

print(good_animals)
