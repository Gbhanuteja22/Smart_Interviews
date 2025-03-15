t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    res=((1<<x)-1)<<y
    print(res%1000000007)
