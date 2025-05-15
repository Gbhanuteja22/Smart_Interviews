from collections import deque
class node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data

def build(arr,i,n):
    if i>n:
        return None
    nn=node(arr[i])
    nn.left=build(arr,2*i,n)
    nn.right=build(arr,2*i+1,n)
    return nn

def countbst(root):
    if not root:
        return True,float("inf"),float("-inf"),0
    lbst,lmin,lmax,lbstcount=countbst(root.left)
    rbst,rmin,rmax,rbstcount=countbst(root.right)
    currbst=lbst and rbst and(lmax<root.data<rmin)
    if currbst:
        total=1+lbstcount+rbstcount
        return True,min(lmin,root.data,rmin),max(lmax,root.data,rmax),total
    else:
        return False,0,0,lbstcount+rbstcount


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr=[0]+arr
    root=build(arr,1,n)
    _,_,_,totbst=countbst(root)
    print(totbst)
