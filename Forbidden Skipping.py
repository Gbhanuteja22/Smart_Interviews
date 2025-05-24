import sys
sys.setrecursionlimit(10**5)
def func(i,choice,arr,dp):
    if i==n:
        return 0
    if dp[i][choice]!=-1:
        return dp[i][choice]
    if choice==0:
        dp[i][choice]=func(i+1,1,arr,dp)+arr[i]
    else:
        take=func(i+1,1,arr,dp)+arr[i]
        skip=func(i+1,0,arr,dp)
        dp[i][choice]=max(take,skip)
    return dp[i][choice]

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    dp=[[-1 for _ in range(2)] for _ in range(n+1)]
    print(func(0,1,arr,dp))
