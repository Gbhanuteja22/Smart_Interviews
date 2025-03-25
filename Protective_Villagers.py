def valid(arr,mid,k):
    prev=arr[0]
    idx=1
    count=1
    while(idx<len(arr)):
        if(arr[idx]-prev>=mid):
            count+=1
            prev=arr[idx]
        idx+=1
    return count>=k
t=int(input())
for _ in range(t):
    n,c=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    low=1
    ans=-1
    high=max(arr)-min(arr)
    while(low<=high):
        mid=(low+high)//2
        if(valid(arr,mid,c)):
            low=mid+1
            ans=mid
        else:
            high=mid-1
    print(ans)
