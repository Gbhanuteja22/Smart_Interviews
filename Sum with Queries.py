t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    q=int(input())
    diff=[0]*(n+1)
    for _ in range(q):
        i,j,x=map(int,input().split())
        diff[i]+=x
        if j+1<n:
            diff[j+1]-=x
    curr=0
    for k in range(n):
        curr+=diff[k]
        arr[k]+=curr
    print(sum(arr))
