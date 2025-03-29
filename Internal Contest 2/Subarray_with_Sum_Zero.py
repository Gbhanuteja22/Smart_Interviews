t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    tot,maxlen,idxmap=0,0,{}
    for i,num in enumerate(arr):
        tot+=num
        if tot==0:
            maxlen=i+1
        elif tot in idxmap:
            maxlen=max(maxlen,i-idxmap[tot])
        else:
            idxmap[tot]=i
    print(maxlen)
