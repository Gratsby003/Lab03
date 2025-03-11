import time
from operator import contains

import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
       self.dictionary=d.Dictionary()

    def printDic(self, language):
        pass

    def getDictionary(self, language):
        dizionario = []
        if language == "Italiano":
            dizionario = self.dictionary.itaDict
        elif language == "Inglese":
            dizionario = self.dictionary.engDict
        elif language == "Spagnolo":
            dizionario = self.dictionary.espDict
        return dizionario

    def searchWord(self, words, language):
        startTime=time.time()
        dizionario = self.getDictionary(language)
        listaErrori = []
        for p in words:
            r=rw.RichWord(p)
            if  contains(dizionario,p):
                r.corretta=True
            else:
                r.corretta=False
            listaErrori.append(r)
        endTime=time.time()
        tempo=endTime-startTime
        return (listaErrori, tempo)

    def searchLinear(self, words, language):
        startTime = time.time()
        dizionario = self.getDictionary(language)
        listaErrori = []
        for p in words:
            r = rw.RichWord(p)
            if p in dizionario:
                r.corretta = True
            else:
                r.corretta = False
            listaErrori.append(r)
        endTime = time.time()
        tempo = endTime - startTime
        return (listaErrori, tempo)

    def searchDichotomic(self, words, language):
        startTime = time.time()
        dizionario = self.getDictionary(language)
        listaErrori = []
        corretta=""
        for p in words:
            corretta=dizionario[(len(dizionario)-1)%2]
            if p==corretta:
                r = rw.RichWord(p)
                r.corretta = True
                listaErrori.append(r)
                break
            elif p<corretta:
                dizionario=dizionario[0:(len(dizionario)-1)%2]
                if p in dizionario:
                    r=rw.RichWord(p)
                    r.corretta=True
                    listaErrori.append(r)
                    break
                continue
            elif p > corretta:
                dizionario=dizionario[(len(dizionario)-1)%2:len(dizionario)-1]
                if p in dizionario:
                    r=rw.RichWord(p)
                    r.corretta=True
                    listaErrori.append(r)
                    break
            r=rw.RichWord(p)
            r.corretta=False
            listaErrori.append(r)
        endTime = time.time()
        tempo = endTime - startTime
        return (listaErrori, tempo)







