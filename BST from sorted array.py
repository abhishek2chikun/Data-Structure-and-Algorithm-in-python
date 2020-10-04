class BST:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def printBST(root):
    if root is None:
        return 
    print(root.value,end="->")
    printBST(root.left)
    printBST(root.right)
def buildBST(array):
    if not array:
        return None
    mid=int(len(array)/2)
    root=BST(array[mid])
    root.left=buildBST(array[0:mid])
    root.right=buildBST(array[mid+1:])
    return root
arr=[1,2,3,4,5,6,7,8,9]
print(arr)
printBST(buildBST(arr))
print()