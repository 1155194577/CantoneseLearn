import jsonpickle

class Word:
    def __init__(self,Cantonese,English) -> None:
        self.name = {"Cantonese":Cantonese,"English":English}
        self.soundtrack = None
        self.score = 0
        self.IsTaught = False
        
    def __str__(self) -> str:
        return f"{self.name["Cantonese"]} -> {self.name["English"]} | has a score : {self.score}"

    def ChangeByOne(self,IsIncrement=True): 
        if (IsIncrement):
            self.score+=1 
        else: 
            self.score-=1 
    
    def TeachPronounication(self): 
            pass

new = Word("你好","Hello")

serialized = jsonpickle.encode(new)
print(serialized)