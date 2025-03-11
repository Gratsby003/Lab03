class Dictionary:
    def __init__(self):
        self.itaDict=self.loadDictionary("Italian.txt")
        self.engDict=self.loadDictionary("English.txt")
        self.espDict=self.loadDictionary("Spanish.txt")

    def loadDictionary(self,path):
        lista=[]
        stringa="resources/"+path
        with open(stringa,'r', encoding="utf-8") as file:
            lista=[p.strip() for p in file.readlines()]
        return lista

    def printAll(self):
        pass
