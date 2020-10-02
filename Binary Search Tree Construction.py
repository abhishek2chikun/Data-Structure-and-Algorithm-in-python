class BST:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    def search(self,value):
        curr=self
        while curr is not None:
            if value<curr.value:
                curr=curr.left
            elif value>curr.value:
                curr=curr.right
            else:
                return "Found"
        return "Not Found"
    def insert(self,value):
        curr=self
        while True:
            if value < curr.value:
                if curr.left is None:
                    curr.left=BST(value)
                    break
                else:
                    curr=curr.left
            else:
                if value > curr.value:
                    if curr.right is None:
                        curr.right=BST(value)
                        break
                    else:
                        curr=curr.right
        return self
    def remove(self,value,parent=None):
        curr=self
        while True:
            if value<curr.value:
                parent=curr
                curr=curr.left
            elif value>curr.value:
                parent=curr
                curr=curr.right
            else:
                if curr.left is not None and curr.right is not None:
                    curr.value=curr.right.get_Min()
                    curr.right.remove(curr.value,curr)
                elif parent is None:
                    if curr.left is not None:
                        curr.value=curr.left.value
                        curr.right=curr.left.right
                        curr.left=curr.left.left
                    elif curr.right is not None:
                        curr.value=curr.right.value
                        curr.left=curr.right.left
                        curr.right=curr.right.right
                    else:
                        curr=None
                elif parent.left==curr:
                    parent.left=curr.left if curr.left is not None else curr.right
                elif parent.right==curr:
                    parent.right=curr.left if curr.right is not None else curr.left
                break
    def get_Min(self):
        curr=self
        while curr.left is not None:
            curr=curr.left
        return curr.value
def traverse(root,inn,pre):
    return "Inorder:{0}\nPreorder:{1}".format(inordertraverse(root,inn),pretraverse(root,pre))
def inordertraverse(root,inn):
    if root is not None:
        inordertraverse(root.left,inn)
        inn.append(root.value)
        inordertraverse(root.right,inn)
    return inn
def pretraverse(root,pre):
    if root is not None:
        pre.append(root.value)
        pretraverse(root.left,pre)
        pretraverse(root.right,pre)
    return pre
tree=BST(50)
tree.insert(70);tree.insert(100);tree.insert(40);
tree.insert(2);tree.insert(-10);
inorder=[];preorder=[];
print(traverse(tree,inorder,preorder))
tree.remove(2);inorder=[];preorder=[];
print("After Deleting 2 from tree")
print(traverse(tree,inorder,preorder))