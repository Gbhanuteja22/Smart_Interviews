def valid(cnta,cntb):
    for i in range(26):
        if(cnta[i]>cntb[i]):
            return False
    return True
t=int(input())
for _ in range(t):
    a,b=map(str,input().split())
    p1=0
    p2=0
    cnta=[0]*(26)
    cntb=[0]*(26)
    for i in range(len(a)):
        cnta[ord(a[i])-97]+=1
    ans=float("inf")
    if sorted(a)==sorted(b):
        print(len(a))
        continue
    n=len(b)
    while(p2<n):
        cntb[ord(b[p2])-97]+=1
        while(valid(cnta,cntb)):
            ans=min(p2-p1+1,ans)
            cntb[ord(b[p1])-97]-=1
            p1+=1
        p2+=1
    if ans==float("inf"):
        print("-1")
    else:
        print(ans)
