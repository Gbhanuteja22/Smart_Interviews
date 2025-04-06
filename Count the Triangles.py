t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    count=0
    for k in range(n-1,-1,-1):
        i=0
        j=k-1
        while(i<j):
            if(arr[i]+arr[j]>arr[k]):
                count+=(j-i)
                j-=1
            else:
                i+=1
    print(count)
