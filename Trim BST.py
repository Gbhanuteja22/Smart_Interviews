from collections import deque
class node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
def insert(root,data):
    if not root:
        return node(data)
    if(root.data<data):
        root.right=insert(root.right,data)
    else:
        root.left=insert(root.left,data)
    return root

def trim(root,l,r):
    if not root:
        return
    if root.data<l:
        return trim(root.right,l,r)
    if root.data>r:
        return trim(root.left,l,r)
    root.left=trim(root.left,l,r)
    root.right=trim(root.right,l,r)
    return root

def preord(root):
    if not root:
        return
    print(root.data,end=" ")
    preord(root.left)
    preord(root.right)

t=int(input())
for _ in range(t):
    n,l,r=map(int,input().split())
    arr=list(map(int,input().split()))
    root=None
    for i in arr:
        root=insert(root,i)
    root=trim(root,l,r)
    preord(root)
    print()
