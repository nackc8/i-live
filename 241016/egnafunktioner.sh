#!/bin/bash

# Om filen endast innehåller funktioner som jag vill använda,
# så ska inga funktionsanrop göras när den läses. Det innebär
# att endast funktionens definition finns i filen.

greet() {
    for namn in "$@"; do # "$@" => "$1" "$2" "$3" ...
        echo "Hej1 $namn"
    done
    return 0 # exitkod 0, det gick bra
}
