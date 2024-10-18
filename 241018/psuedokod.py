# Mål: Byt ut repeterande specialtecken som :,.; och mellanslag mot endast ett tecken i
# en fil som användaren anger och skriv ut det till stdout.

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

# Mål: Byt ut repeterande specialtecken som :,.; och mellanslag mot endast ett tecken i
# en fil som användaren anger och skriv ut det till stdout.

non_repeating_chars = ":,.; "

# för varje line i file_lines
#    hitta repeterande non_repeating_chars i
#    line, och uppdatera line med en version där endast sådant tecken är i följd.
