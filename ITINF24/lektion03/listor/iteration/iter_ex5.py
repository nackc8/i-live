#!/usr/bin/env python3

animals = ["donkey", "giraffe", "monkey", "pinguin", "armadillo"]

good_animals = [animal for animal in animals]

# Exakt samma som:
#
# good_animals = []
# for animal in animals:
#     good_animals.append(animal * 2)

print(good_animals)
