class GenericTree:
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
n1=GenericTree(50)
n2=GenericTree(10)
n3=GenericTree(20)
n4=GenericTree(30)
n5=GenericTree(5)
n6=GenericTree(15)
n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n2.children.append(n5)
n4.children.append(n6)
printTree(n1)
