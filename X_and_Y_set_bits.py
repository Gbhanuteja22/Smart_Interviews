t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    n=(1<<x)|(1<<y)
    print(n%1000000007)
