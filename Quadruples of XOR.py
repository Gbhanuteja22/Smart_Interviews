from collections import defaultdict
t=int(input())
for _ in range(t):  
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    d=list(map(int,input().split()))
    xorpairs=defaultdict(int)
    for i in range(n):
        for j in range(n):
            xorval=a[i]^b[j]
            xorpairs[xorval]+=1
    count=0
    for i in range(n):
        for j in range(n):
            xorval=c[i]^d[j]
            if xorval in xorpairs:
                count+=xorpairs[xorval]
    print(count)
