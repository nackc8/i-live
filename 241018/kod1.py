# Mål: Byt ut repeterande specialtecken som :,.; och mellanslag mot endast ett tecken i
# en fil som användaren anger och skriv ut det till stdout.

# Filen körbar med: chmod +x kod1.py

# om användaren inte har angett något argument
#    skriv ett felmeddelande till stderr
#    avsluta med en statuskod som betyder att det blev fel

# om användaren har anget fler än ett argument
#    skriv ett felmeddelande till stderr
#    avsluta med en statuskod som betyder att det blev fel

# input = argumentet som användaren angav

# om filen input inte finns eller inte kan läsas
#    skriv ett felmeddelande till stderr
#    avsluta med en statuskod som betyder att det blev fel

# file_lines = läs in alla rader i filen "input" till en lista med strängar

# non_repeating_chars = ":,.; "

# för varje line i file_lines
#    parts = en lista av de delar inom line där non_repeating_chars repeteras
#    för varje part i parts
#       line =
#         - Den nuvarande line, fast med delen part utbytt mot ett tecken.
#         - Det tecknet kan tas från första positionen i part.

# Notering: nu har vi en lines där radernas repeterande
#           non_repeating_chars-tecken bytts ut mot endast ett

# Skriv ut alla lines som en sträng

# Avsluta med en statuskod som betyder att det gick bra
