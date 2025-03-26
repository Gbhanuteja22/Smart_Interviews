t=int(input())
for _ in range(t):
    n=int(input())
    count=0
    length=0
    arr=list(map(int,input().split()))
    for i in range(n):
        mini=arr[i]
        maxi=arr[i]
        for j in range(i,n):
            maxi=max(maxi,arr[j])
            mini=min(mini,arr[j])
            if((maxi-mini)+1==j-i+1):
                length=max(j-i+1,length)
    print(length)
