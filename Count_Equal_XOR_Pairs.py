t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    d={}
    for i in range (n):
        xor=a[i]^b[i]
        if xor in d:
            d[xor]+=1
        else:
            d[xor]=1
    count=0
    for i in d.values():
        for x in range(1,i):
            count+=x
    print(count)
