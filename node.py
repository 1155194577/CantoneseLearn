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

## write a function , that convert any sentence to Binary Tree 
## if subarr.len == 2 => flatten subarr and createnode. 
## if subarr.len == 2 && childrens are str && not list => return; 
arr = [["excuse me","miss"],[["are you","American"],["?"]]]
concated = flatten(arr)
print(concated)
print(" ".join(concated))
root = None
def CreateTree(arr): 
    flated = flatten(arr)
    concated = " ".join(flated)
    curr = WordNode(English=concated)
    global root 
    root= curr
    print(WordNode)
    length = len(arr)
    if (length==1):
        if isinstance(arr[0],str):
            WordNode(English=arr[0],parent=curr)
        else:
            CreateTree(arr[0])
    elif (length == 2):
        if isinstance(arr[0],str):
            WordNode(English=arr[0],parent=curr)
        else: 
            CreateTree(arr[0])
        if isinstance(arr[1],str):
            WordNode(English=arr[1],parent=curr)
            CreateTree(arr[1])
            
CreateTree(arr)

for pre, _, node in RenderTree(root):
    print("%s%s" % (pre, node.name))