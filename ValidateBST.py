class BST:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
def validateBST(root):
    return validate(root,Min=float("-inf"),Max=float("inf"))
def validate(root,Min,Max):
    if root is None:
        return True
    if root.value < Min or root.value > Max:
        return False
    left_validate=validate(root.left,Min,root.value)
    return left_validate and validate(root.right,root.value,Max)  
tree=BST(10,left=BST(5,left=BST(1),right=BST(7)),right=BST(15,left=BST(11),right=BST(18)))
def check(root):
    if validateBST(root) == True:
        return f"Your tree is BST!!!!!"
    else:
        return f"Sorry your tree is not a BST"
print(check(tree))
tree.left.left.left=BST(100)
print(check(tree))