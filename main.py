import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano:")
        frase = input()
        sc.handleSentence(frase,"Italiano")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese:")
        frase = input()
        sc.handleSentence(frase,"Inglese")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo:")
        frase = input()
        sc.handleSentence(frase,"Spagnolo")
        continue

    if int(txtIn) == 4:
        break


