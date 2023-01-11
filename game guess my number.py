import random

print("Willkommen im Spiel 'Zahlen erraten'.")
print("Computer überlegt sich eine Zahl...")
randInteger = random.randrange(1, 1000)

print("Fertig. Ich habe mir eine Zahl zwischen 1 - 1000 überlegt")
print("Sie können das Spiel jederzeit mit der Eingabe '0' beenden.")

guessedNumber = -1
tries = 0

while randInteger != guessedNumber:
    guessedNumber = int( input("Errate die Zahl: ") )

    #stop the game
    if guessedNumber == 0:
        print("Das Spiel wird abgebrochen")
        break;

    #give a hint
    if guessedNumber > randInteger:
        print("Deine Zahl ist größer als meine.")
    elif guessedNumber < randInteger:
        print("Deine Zahl ist kleiner als meine.")

    tries += 1
else:
    print("Super. Du hast meine Zahl erraten", randInteger, ". Du hast", tries, "Versuche gebraucht.")
