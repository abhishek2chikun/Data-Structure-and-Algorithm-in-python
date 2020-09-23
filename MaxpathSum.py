class BinaryTree:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left
def MaxpathSum(root):
    if root is None:
        return (0,0)
    ll,l=MaxpathSum(root.left)
    rr,r=MaxpathSum(root.right)
    maxchild=max(ll,rr)
    value=root.data
    maxbranch=max(maxchild+value,value)
    maxtri=max(ll+rr+value,maxbranch)
    maxpath=max(maxtri,l,r)
    return (maxbranch,maxpath)
    
root=BinaryTree(1,left=BinaryTree(2,left=BinaryTree(4),right=BinaryTree(5)),right=BinaryTree(3,left=BinaryTree(6),right=BinaryTree(7)))
print("Max path of Tree is:")
print(MaxpathSum(root)[1])
root1=BinaryTree(-20,left=BinaryTree(40,left=BinaryTree(100),right=BinaryTree(500)),right=BinaryTree(-200))
print("Max path of Tree is:")
print(MaxpathSum(root1)[1])