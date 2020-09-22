class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
def preiter(root):
    stack=[]
    temp=root
    while temp is not None or len(stack):
        while(temp is not None):
            print(temp.data,end="-")
            if temp.right is not None:
                stack.append(temp.right)
            temp=temp.left
        if stack:
            temp=stack.pop()
def preiterN(root):
    if root is None:
        return
    stack=[]
    stack.append(root)
    while stack:
        temp=stack.pop()
        print(temp.data,end="-")
        if temp.right is not None:
            stack.append(temp.right)
        if temp.left is not None:
            stack.append(temp.left)
root=Node(1,right=Node(3),left=Node(2,right=Node(5),left=Node(4)))
print("Preorder with aux space complexity H:")
preiter(root)
print("\nPreorder with aux space complexity N:")
preiterN(root)
print()