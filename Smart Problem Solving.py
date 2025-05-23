t=int(input())
for _ in range(t):
    n=int(input())
    p=[]
    s=[]
    for _ in range(n):
        u,v=map(int,input().split())
        p.append(u)
        s.append(v)
    dp=[0 for _ in range(n+100)]
    for i in range(n-1,-1,-1):
        dp[i]=max(dp[i+1],p[i]+dp[i+s[i]+1])
    print(dp[0])
