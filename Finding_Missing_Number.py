t=int(input())
for _ in range(t):
    n=int(input())
    res=0
    for i in range(1,n+2):
        res^=i
    arr=list(map(int,input().split()))
    for i in arr:
        res^=i
    print(res)
