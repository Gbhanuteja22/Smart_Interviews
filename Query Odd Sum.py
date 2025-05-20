t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    prefix=[0]*(n+1)
    for i in range(1,n+1):
        prefix[i]=prefix[i-1]+arr[i-1]
    for _ in range(q):
        i,r,k=map(int,input().split())
        rangesum=prefix[r+1]-prefix[i]
        sol=prefix[n]-rangesum
        sol+=(r-i+1)*k
        if(sol%2==1):
            print("YES",sol)
        else:
            print("NO")
