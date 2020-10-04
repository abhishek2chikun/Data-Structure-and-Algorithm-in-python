class BST:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
def path(root,k,l=[]):
    if root is None:
        return None
    if root.value==k:
        l.append(root.value)
        return l
    leftnode=path(root.left,k,l)
    if leftnode!=None:
        l.append(root.value)
        return leftnode
    rightnode=path(root.right,k,l)
    if rightnode!=None:
        l.append(root.value)
        return rightnode
    else:
        return None
tree=BST(10,left=BST(5,left=BST(1),right=BST(7)),right=BST(15,left=BST(11),right=BST(18)))
print(path(tree,18,[]))
tree.left.left.left=BST(-1,left=BST(-10),right=BST(0))
tree.left.left.right=BST(2)
print(path(tree,0,[]))