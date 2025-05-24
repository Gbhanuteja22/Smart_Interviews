m=10**9+7
maxi=10**6+7
dp0=[0]*(maxi)
dp1=[0]*(maxi)
dp0[0]=1
for i in range(1,maxi):
    dp0[i]=dp0[i-1]
    if i>=2:
        dp0[i]=(dp0[i]+dp0[i-2])%m 
    dp1[i]=dp1[i-1]
    if i>=1:
        dp1[i]=dp1[i-1]
    if i>=2:
        dp1[i]=(dp1[i]+dp1[i-2])%m 
    if i>=3:
        dp1[i]=(dp1[i]+dp0[i-3])%m 

t=int(input())
for _ in range(t):
    n=int(input())
    print((dp0[n]+dp1[n])%m)
