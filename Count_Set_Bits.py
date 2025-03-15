t=int(input())
for _ in range(t):
    n=int(input())
    count=0
    while(n>0):
        n=n&(n-1)
        count+=1
    print(count)
