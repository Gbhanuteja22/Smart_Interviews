def valid(arr,mid,k):
    currsum=0
    for i in range(0,n):
        if (arr[i]>mid):
            d=abs(arr[i]-mid)
            currsum+=d
        if currsum>=k:
            return True
    return False
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    start=1
    ans=-1
    end=max(arr)
    while(start<=end):
        mid=(start+end)//2
        if(valid(arr,mid,k)==1):
            ans=mid
            start=mid+1
        else:
            end=mid-1
    print(ans)
