t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=0
    for i in range(n):
        maxi=float("-inf")
        mini=float("inf")
        d=set()
        for j in range(i,n):
            maxi=max(arr[j],maxi)
            mini=min(arr[j],mini)
            d.add(arr[j])
            if(maxi-mini==(len(d))-1):
                ans=max(ans,len(d))
    print(ans)
