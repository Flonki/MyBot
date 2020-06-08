
class Lebewesen:
    def __init__(self,name:str,alter:int):
        print("Ein LebeWesen Wurde Erschaffen")
        self.name = name
        self.alter = alter

class Mensch(Lebewesen):
    def __init__(self,name:str,alter:int):
        super().__init__(name,alter)
        self.name = name
        self.alter = alter

    def sage(self,nachricht:str):
        print(self.name+':'+nachricht)

katze = Lebewesen("Minka",7)
print(katze.alter)

florian = Mensch("Florian",13)
florian.sage("Test")
