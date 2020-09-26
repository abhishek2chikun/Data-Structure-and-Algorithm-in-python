class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
def ChildSum(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return True
    if root.left is not None:
        suml=root.left.data
    if root.right is not None:
        sumr=root.right.data
    return ((root.data==suml+sumr) and ChildSum(root.left) and ChildSum(root.right))
root=Node(10,left=Node(7,left=Node(4),right=Node(3)),right=Node(3,left=Node(2),right=Node(1)))
print(ChildSum(root))