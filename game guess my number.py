import random

print("Willkommen im Spiel 'Zahlen erraten'.")
print("Computer überlegt sich eine Zahl...")
randInteger = random.randrange(1, 1000)

print("Fertig. Ich habe mir eine Zahl zwischen 1 - 1000 überlegt")

guessedNumber = 0
tries = 0

while randInteger != guessedNumber:
    guessedNumber = int( input("Errate die Zahl: ") )

    if guessedNumber > randInteger:
        print("Deine Zahl ist größer als meine.")

    if guessedNumber < randInteger:
        print("Deine Zahl ist kleiner als meine.")

    tries += 1

print("Super. Du hast meine Zahl erraten", randInteger, ". Du hast", tries, "Versuche gebraucht.")
