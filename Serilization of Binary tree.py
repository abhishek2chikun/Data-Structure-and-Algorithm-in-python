class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left
class Serilization:
    def __init__(self):
         self.list=[]

    def preorder(self,root):
        if root is None:
            self.list.append(-1)
            return
        self.list.append(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
        return self.list
root=Node(1,right=Node(3),left=Node(2,left=Node(4),right=Node(5)))
s=Serilization()
print(s.preorder(root))
