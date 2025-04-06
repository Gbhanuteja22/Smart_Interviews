t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    sumi=0
    for i in range(len(arr)):
        sumi+=arr[i]*(i+1)*(n-i)
    print(sumi)
