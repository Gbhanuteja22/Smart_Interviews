for _ in range(int(input())):
    n,m=map(int,input().split())
    d={}
    count=0
    for _ in range(n):
        s=input()
        k=str(sorted(s))
        if k in d:
            d[k]+=1
        else:
            d[k]=1
            count+=1
    print(count)
