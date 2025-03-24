def check(arr,mid,k):
    currsum=0
    count=1
    for i in arr:
        currsum+=i
        if(currsum>mid):
            currsum=i
            count+=1
            if (count>k):
                return False
    return True
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    low=max(arr)
    high=sum(arr)
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        if(check(arr,mid,k)):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    print(ans)
