#!/bin/bash

funktionsnamn1() {
    for namn in "$@"; do # "$@" => "$1" "$2" "$3" ...
        echo "Hej1 $namn"
    done
    return 0 # exitkod 0, det gick bra
}

funktionsnamn2() {
    for namn; do
        echo "Hej2 $namn"
    done
    return 1 # exitkod 1, det INTE gick bra
}

funktionsnamn1 Pelle Mayank
funktionsnamn2 Pelle Mayank
