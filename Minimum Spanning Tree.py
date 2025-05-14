import heapq
def func(n,edges):
    pq=[(0,1)]
    vis=[False]*(n+1)
    tot=0
    while(pq):
        w,u=heapq.heappop(pq)
        if vis[u]:
            continue
        tot+=w
        vis[u]=True
        for v,w in edges[u]:
            if not vis[v]:
                heapq.heappush(pq,(w,v))
    return tot
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    edges=[[]for _ in range(n+1)]
    for _ in range(m):
        u,v,w=map(int,input().split())
        edges[u].append((v,w))
        edges[v].append((u,w))
    print(func(n,edges))
