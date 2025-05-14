t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    stk=[]
    span=[0]*n
    for i in range(n):
        while stk and arr[stk[-1]]<=arr[i]:
            stk.pop()
        if stk:
            span[i]=i-stk[-1]
        else:
            span[i]=i+1
        stk.append(i)
    print(*span)
