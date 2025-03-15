t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    n=a^b
    count=0
    while(n>0):
        n=n&(n-1)
        count+=1
    print(count)
