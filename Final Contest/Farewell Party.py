t=int(input())
for _ in range(t):
    n=int(input())
    times=[]
    for i in range(n):
        a,d=map(int,input().split())
        times.append((a,1))
        times.append((d+1,-1))
    times.sort()
    curr=0
    maxi=0
    for t,dx in times:
        curr+=dx
        maxi=max(maxi,curr)
    print(maxi)
