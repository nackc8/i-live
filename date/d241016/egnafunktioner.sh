# shellcheck disable=SC2317

# Om filen endast innehåller funktioner som jag vill använda,
# så ska inga funktionsanrop göras när den läses. Det innebär
# att endast funktionens definition finns i filen.

# Vi ska inte anropa den:
# chmod -x egnafunktioner.sh

greet() {
    for namn in "$@"; do # "$@" => "$1" "$2" "$3" ...
        echo "Hej1 $namn"
    done
    return 0 # exitkod 0, det gick bra
}

# Får tillgång till att använda funktionen, lägg in i .bashrc
#   source /home/kent/i-live/ITINF23/lektion2/egnafunktioner.sh
