s=input()
q=int(input())
queries=list(map(int,input().split()))
curr=[]
n=len(s)
tot=0
for i in range(n):
    tot+=n-i 
    curr.append(tot)
for k in queries:
    if k>curr[-1]:
        print(-1)
        continue
    low=0
    high=n-1
    while(low<high):
        mid=(low+high)//2
        if(curr[mid]<k):
            low=mid+1
        else:
            high=mid
    start=low
    prev=curr[start-1] if start>0 else 0
    length=k-prev
    print(s[start:start+length])
