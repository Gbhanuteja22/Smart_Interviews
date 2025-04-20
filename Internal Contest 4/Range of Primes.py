import math
arr=[1]*((10**6)+1)
for i in range(2,(10**3)+1):
    if(arr[i]==1):
        for j in range(i*i,10**6,i):
            if(arr[j]==1):
                arr[j]=0
presum=[0]*(10**6)
presum[0]=0
presum[1]=0
for i in range(2,len(arr)-1):
    presum[i]=presum[i-1]+arr[i]

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    print(presum[b]-presum[a-1])
