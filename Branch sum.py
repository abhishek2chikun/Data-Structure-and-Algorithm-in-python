class BinaryTree:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left
def BranchSum(root):
    sum=[]
    branch(root,0,sum)
    return sum
def branch(root,runningsum,sum):
    if root is None:
        return
    newsum=runningsum+root.data
    if root.left is None and root.right is None:
        sum.append(newsum)
    branch(root.left,newsum,sum)
    branch(root.right,newsum,sum)
        
root=BinaryTree(1,left=BinaryTree(2,left=BinaryTree(10),right=BinaryTree(20)),right=BinaryTree(3,left=BinaryTree(30),right=BinaryTree(40)))
print("Sum of each branch is:",BranchSum(root))
root1=BinaryTree(10,left=BinaryTree(20,left=BinaryTree(30),right=BinaryTree(40)))
print("Sum of each branch is:",BranchSum(root1))
root2=BinaryTree(10,left=BinaryTree(20),right=BinaryTree(30))
print("Sum of each branch is:",BranchSum(root2))