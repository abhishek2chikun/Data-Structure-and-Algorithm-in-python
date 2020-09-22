class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
def post2stack(root):
    s1=[]
    s2=[]
    s1.append(root)
    while s1:
        temp=s1.pop()
        s2.append(temp)
        if temp.left is not None:
            s1.append(temp.left)
        if temp.right is not None:
            s1.append(temp.right)
    while s2:
        temp=s2.pop()
        print(temp.data,end="->")
def peek(s1):
    if len(s1)>0:
        return s1[-1]
    return None
def post1stack(root):
    s1=[]
    while True:
        while(root):
            if root.right is not None:
                s1.append(root.right)
            s1.append(root)
            root=root.left
        root=s1.pop()
        if root.right is not None and peek(s1)==root.right:
            s1.pop()
            s1.append(root)
            root=root.right
        else:
            print(root.data,end="->")
            root=None
        if len(s1)==0:
            break
root=Node(1,right=Node(3),left=Node(2,right=Node(5),left=Node(4)))
print("Postorder using 2 stack:")
post2stack(root)
print("\nPostorder using ! stack:")
post1stack(root)
print()