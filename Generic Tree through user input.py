class GenericTreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()
def printTree(root):
    if root is None:
        return 
    print(root.data,":",end="")
    for child in root.children:
        print(child.data,",",end="")
    print()
    for child in root.children:
        printTree(child)
def TakeInput():
    rootdata=int(input("Enter the node data:"))
    root=GenericTreeNode(rootdata)
    x=int(input(f"Enter the no. child of {root.data}:"))
    for i in range(0,x):
        child=TakeInput()
        root.children.append(child)
    return root
root=TakeInput()
printTree(root)
