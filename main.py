from anytree import Node, RenderTree, PostOrderIter
from Nest import flatten
from node import WordNode

def Arr2str(arr): 
    if (isinstance(arr,str)):
        return arr
    return " ".join(flatten(arr))


def CreateTree(arr):
    root = WordNode(English = Arr2str(arr), Cantonese="debug")
    leftarr,rightarr = arr[0],arr[1]
    ##print(isinstance(leftarr,str),isinstance(rightarr,str))
    if isinstance(leftarr,str):
        rootl = WordNode(English=Arr2str(leftarr),Cantonese="debug",parent=root)
    else:    
        rootl = CreateTree(leftarr)
        rootl.parent = root   
    if isinstance(rightarr,str):
        rootr = WordNode(English=Arr2str(rightarr),Cantonese="debug",parent=root)
    else:
        rootr = CreateTree(rightarr)
        rootr.parent = root 
    return root

arr2= [["excuse me","miss"],["Are you",["American","?"]]]
root = CreateTree(arr2)

def translate(eng):
    Hashmap = { 
        "excuse me":"請問",
        "miss":"小姐",
        "Are you":"你係唔係",
        "American ?":"美國人啊?",
        "American":"美國人",
        "?":"啊?",
        'excuse me miss Are you American ?':"請問小姐, 你係唔係美國人啊?",
        'excuse me miss':"請問小姐",
        'Are you American ?':"你係唔係美國人啊?",
        }
    return Hashmap[eng]

map(translate, ["excuse me","are you","American","?"])

for pre, fill, node in RenderTree(root):
    Eng_word = node.name["English"]
    print("%s%s (%s)" % (pre, Eng_word,translate(Eng_word)))

postarr = [node.name["English"] for node in PostOrderIter(root)]
for word in postarr:
    print(word)