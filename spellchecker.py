
from operator import contains
from traceback import print_tb

import multiDictionary as md
from dictionary import Dictionary


class SpellChecker:

    def __init__(self):
        self.multiDictionary= md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        txtIn=replaceChars(txtIn.lower())
        parole=txtIn.split(" ")
        lista=self.multiDictionary.searchWord(parole, language)
        listaErrori=lista[0]
        contatore=0
        print("Parole errate:")
        for p in listaErrori:
            corr=p.corretta
            if not corr:
                print(str(p))
                contatore+=1
        print(f"Numero errate: {contatore}")
        print(f"Tempo per lo svolgimento: {lista[1]}")
        print("-----------------------------------------------------")
        lista = self.multiDictionary.searchLinear(parole, language)
        listaErrori = lista[0]
        contatore = 0
        print("Parole errate:")
        for p in listaErrori:
            corr = p.corretta
            if not corr:
                print(str(p))
                contatore += 1
        print(f"Numero errate: {contatore}")
        print(f"Tempo per lo svolgimento: {lista[1]}")
        print("----------------------------------------------------------")
        lista = self.multiDictionary.searchDichotomic(parole, language)
        listaErrori = lista[0]
        contatore = 0
        print("Parole errate:")
        for p in listaErrori:
            corr = p.corretta
            if not corr:
                print(str(p))
                contatore += 1
        print(f"Numero errate: {contatore}")
        print(f"Tempo per lo svolgimento: {lista[1]}")



    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text