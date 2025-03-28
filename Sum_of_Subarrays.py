n=int(input())
arr=list(map(int,input().split()))
presum=[0]*n
presum[0]=arr[0]
for i in range(1,n):
    presum[i]=presum[i-1]+arr[i]
for i in range(int(input())):
    i,j=map(int,input().split())
    if i==0:
        print(presum[j])
    else:
        print(presum[j]-presum[i-1])
