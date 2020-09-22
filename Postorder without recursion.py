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
root=Node(1,right=Node(3),left=Node(2,right=Node(5),left=Node(4)))
print("Postorder using 2 stack:")
post2stack(root)
print("\nPreorder with aux space complexity N:")
post2stack(root)
print()