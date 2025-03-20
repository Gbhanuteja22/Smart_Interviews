t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(n-1):
        maxi=0
        for j in range(n-i):
            if(arr[j]>arr[maxi]):
                maxi=j
        arr[maxi],arr[n-i-1]=arr[n-i-1],arr[maxi]
        print(maxi,end=" ")
    print()
