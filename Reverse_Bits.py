t=int(input())
for _ in range(t):
    n=int(input())
    res=0
    for i in range(32):
        res=(res<<1)|(n&1)
        n>>=1
    print(res)
