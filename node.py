import jsonpickle
from anytree import NodeMixin,RenderTree
from Nest import flatten
class WordNode(NodeMixin):
    def __init__(self,Cantonese="NOT",English="NULL",parent=None,children=None) -> None:
        super(WordNode,self).__init__()
        self.name = {"Cantonese":Cantonese,"English":English}
        self.soundtrack = None
        self.score = 0
        self.IsTaught = False
        self.parent = parent
        if children:
            self.children = children
    def __str__(self) -> str:
        return f"{self.name["Cantonese"]} -> {self.name["English"]} | has a score : {self.score}"

    def ChangeByOne(self,IsIncrement=True): 
        if (IsIncrement):
            self.score+=1 
        else: 
            self.score-=1 
    
    def TeachPronounication(self): 
            pass
        
    def append(self,PushedNode):
        try:
              self.name["Cantonese"] = f"{self.name["Cantonese"]}{PushedNode.name["Cantonese"]}" 
              self.name["English"] =  f"{self.name["English"]} {PushedNode.name["English"]}"
            ##  print(self.name)
              return "Appended"
        except:
            print("error")

