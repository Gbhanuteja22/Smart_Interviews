t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(n):
        if(i%2==0):
            for j in range(n):
                print(arr[i][j],end=" ")
        else:
            for j in range(n-1,-1,-1):
                print(arr[i][j],end=" ")
        print()
    
