m=1000000007
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    ans=1
    while(b!=0):
        if(b&1):
            ans=(ans*a)%m
        a=(a*a)%m
        b>>=1
    print(ans%m)
