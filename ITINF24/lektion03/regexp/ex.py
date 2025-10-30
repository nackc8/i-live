#!/usr/bin/env python3

import re

# psuedokod för regex som matchar ord på b:
# (först på raden|tecken som inte är a-z)b(sist på raden|tecken som inte är a-z)
# mer och mer till riktig kod.

# (^|tecken som inte är a-z)b(sist på raden|tecken som inte är a-z)
#  \__ utbytt mot riktig kod

# (^|[^a-z]+)b(sist på raden|[^a-z]+)
#      \__ utbytt mot riktig kod \__ utbytt mot riktig kod

# (^|[^a-z]+)b($|[^a-z]+)
#              \__ utbytt mot riktig kod

# (^|[^a-zA-Z]+)[bB]($|[^a-zA-Z]+)
#                 \__ utbytt mot riktig kod

# re.compile()
