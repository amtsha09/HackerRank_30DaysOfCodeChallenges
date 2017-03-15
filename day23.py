import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
    #Write your code here
    q=[root] if root else []
    
    while q:
        current = q.pop(0)
        print(current.data, end = " ")
        if current.left: q.append(current.left)
        if current.right: q.append(current.right)


if __name__ == '__main__':
    T=int(input())
    myTree=Solution()
    root=None
    for i in range(T):
        data=int(input())
        root=myTree.insert(root,data)
    myTree.levelOrder(root)

