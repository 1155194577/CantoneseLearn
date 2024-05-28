from anytree import Node, RenderTree, PostOrderIter
from Nest import flatten
"""
root = Node("Excuse me Miss, are you American?")
rootl = Node("Excuse me Miss",parent=root)
rootr  = Node("are you American?",parent=root)
rootll = Node("Excuse me",parent=rootl)
rootlr = Node("Miss",parent=rootl)
rootrl = Node("are you",parent=rootr)
rootrr = Node("American?",parent=rootr)
rootrrl = Node("American",parent=rootrr)
rootrrr = Node("?",parent=rootrr)
"""
def Arr2str(arr): 
    ## merge with space , if both are str 
    if (isinstance(arr,str)):
        return arr 
    #if isinstance(arr[0],str) and isinstance(arr[1],str):  
     #   return " ".join(flatten(arr))
    return " ".join(flatten(arr))
    """
    if isinstance(arr[0],str) and isinstance(arr[1],str):
        return "".join(flatten(arr)) 
    return "".join(flatten(arr))
    """
arr = [
    ["Excuse me","Miss"],
    ["Are you",["American","?"]]
]
arr2= [["hello","world"],["programming",["is","fun"]]]
print(Arr2str(arr))

def CreateTree(arr):
    root = Node(Arr2str(arr))
    leftarr,rightarr = arr[0],arr[1]
    print(isinstance(leftarr,str),isinstance(rightarr,str))
    if isinstance(leftarr,str):
        rootl = Node(Arr2str(leftarr),parent=root)
    else:    
        rootl = CreateTree(leftarr)
        rootl.parent = root   
    if isinstance(rightarr,str):
        rootr = Node(Arr2str(rightarr),parent=root)
    else:
        rootr = CreateTree(rightarr)
        rootr.parent = root 
    return root
    
root = CreateTree(arr2)

for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))

print([node.name for node in PostOrderIter(root)])