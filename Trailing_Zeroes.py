t=int(input())
for _ in range(t):
    count=0
    n=int(input())
    while(n>0):
        n//=5
        count+=n
    print(count)