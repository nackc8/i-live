#!/usr/bin/env python3

import re

# psuedokod för regex som matchar ord på b:
# (först på raden|tecken som inte är a-z)b(sist på raden|tecken som är a-z)
# mer och mer till riktig kod.

# (^|tecken som inte är a-z)b(sist på raden|tecken som inte är a-z)
#  \__ utbytt mot riktig kod

# (^|[^a-z]+)b(sist på raden|[a-z]+)
#      \__ utbytt mot riktig kod \__ utbytt mot riktig kod

# (^|[^a-z]+)b($|[^a-z]+)
#              \__ utbytt mot riktig kod

# (^|[^a-zA-Z]+)[bB]($|[a-zA-Z]+)
#                 \__ utbytt mot riktig kod

# Sätt det vi vill ha inom en grupp
# (^|[^a-zA-Z]+)([bB]($|[a-zA-Z]+))
#               \__ start         \___ slut på vill-ha-gruppen

# r-sträng, behåller alla tecken som de är skrivna
ord_re = re.compile(r"(^|[^a-zA-Z]+)([bB]($|[a-zA-Z]+))")

# Jättebra kontrollsida: https://regex101.com/

with open("test.txt") as file:
    content = file.read()

    for match in re.findall(ord_re, content):
        print(match[1])
