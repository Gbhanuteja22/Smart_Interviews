t=int(input())
for _ in range(t):
    n=int(input())
    s=str(bin(n)[2:])
    count=0
    ans=0
    for i in range(len(s)):
        if(i=='1'):
            count+=1
        else:
            ans=max(count,ans)
            count=0
    print(ans)
