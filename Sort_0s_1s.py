t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    for i in arr:
        print(i,end=" ")
    print()
