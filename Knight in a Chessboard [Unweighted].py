def func(a,b,c,d,e,f):
    vis=[[False]*(b+1) for _ in range(a+1)]
    vis[c][d]=True
    q=[]
    q.append((c,d,0))
    dirs=[(1,2),(-1,2),(-1,-2),(1,-2),(2,1),(2,-1),(-2,-1),(-2,1)]
    while(q):
        i,j,c=q.pop(0)
        if(i==e and j==f):
            return c
        for k in dirs:
            ni=i+k[0]
            nj=j+k[1]
            if 1<=ni<=a and 1<=nj<=b and not vis[ni][nj]:
                vis[ni][nj]=True
                q.append((ni,nj,c+1))
    return -1

t=int(input())
for _ in range(t):
    a,b,c,d,e,f=map(int,input().split())
    print(func(a,b,c,d,e,f))
