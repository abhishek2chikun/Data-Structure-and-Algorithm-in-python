class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left
def preorder(root):
    if root is None:
        return
    print(root.data,end="->")
    preorder(root.left)
    preorder(root.right)
i=-1
def Deserilization(str):
    global i
    i+=1
    value=str[i]
    if value==-1:
        return None
    root=Node(value)
    root.left=Deserilization(str)
    root.right=Deserilization(str)
    return root

string=[1, 2, 4, -1, -1, 5, -1, -1, 3, -1, -1]
x=Deserilization(string)
print("Tree is:")
preorder(x)
print()
i=-1
str2=[1,-1,-1]
y=Deserilization(str2)
print("Tree is")
preorder(y)
print()