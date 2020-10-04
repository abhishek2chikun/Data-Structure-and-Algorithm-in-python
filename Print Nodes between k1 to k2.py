class BST:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def printK1_k2(root,k1,k2):
    if root is None:
        return 
    if k1 <= root.value <=k2:
        print(root.value)
    if root.value > k2:
        printK1_k2(root.left,k1,k2)
    elif root.value < k1:
        printK1_k2(root.right,k1,k2)
    else:
        printK1_k2(root.left,k1,k2) 
        printK1_k2(root.right,k1,k2)

tree=BST(10,left=BST(5,left=BST(1),right=BST(7)),right=BST(15,left=BST(11),right=BST(18)))
print("k1=19 k2=16:");printK1_k2(tree,19,16)
print("\nk1=5 k2=10:");printK1_k2(tree,5,10)
print("\nk1=8 k2=20");printK1_k2(tree,8,20)
