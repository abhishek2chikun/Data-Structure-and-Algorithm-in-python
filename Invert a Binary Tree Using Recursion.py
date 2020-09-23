class BinaryTree:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end="->")
        inorder(root.right)

def InvertTree(root):
    if root is None:
        return
    Swap(root)
    InvertTree(root.left)
    InvertTree(root.right)
    return root

def Swap(root):
    root.left,root.right=root.right,root.left

root=BinaryTree(1,left=BinaryTree(2,left=BinaryTree(4),right=BinaryTree(5)),right=BinaryTree(3,left=BinaryTree(6),right=BinaryTree(7)))
print("Tree is:")
a=inorder(root)
print("\nAfter Invert :")
x=InvertTree(root)
b=inorder(x)
print("\nInvert of Invert tree:")
c=inorder(InvertTree(x))
print("\nIs Invert of Invert Tree is equal to Tree :",a==c)