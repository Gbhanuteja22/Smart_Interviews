t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    edges=[[]for _ in range(n+1)]
    for _ in range(m):
        u,v=map(int,input().split())
        edges[u].append(v)
        edges[v].append(u)
    vis=[False]*(n+1)
    sizes=[]
    for i in range(1,n+1):
        if not vis[i]:
            count=0
            vis[i]=True
            q=[]
            q.append(i)
            while(q):
                x=q.pop()
                count+=1
                for v in edges[x]:
                    if not vis[v]:
                        vis[v]=True
                        q.append(v)
            sizes.append(count)
    tot=n*(n-1)//2
    reach=sum(s*(s-1)//2 for s in sizes)
    print(tot-reach) 
