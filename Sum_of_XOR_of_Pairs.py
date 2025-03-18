t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    sumi=0
    for i in range(32):
        count=0
        for j in range(n):
            if((arr[j]>>i)&1):
                count+=1
        unset=n-count
        sumi+=count*unset*(1<<i)
    print(2*sumi)
