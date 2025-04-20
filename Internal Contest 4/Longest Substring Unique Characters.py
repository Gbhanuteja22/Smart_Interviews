t=int(input())
for _ in range(t):
    s=input().lower()
    myset=set()
    low=0
    high=0
    ans=0
    for high in range(len(s)):
        while s[high] in myset:
            myset.remove(s[low])
            low+=1
        ans=max(ans,high-low+1)
        myset.add(s[high])
    print(ans)
