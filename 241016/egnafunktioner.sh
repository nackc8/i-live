#!/bin/bash

greet() {
    for namn in "$@"; do # "$@" => "$1" "$2" "$3" ...
        echo "Hej1 $namn"
    done
    return 0 # exitkod 0, det gick bra
}

greet Pelle Mayank
