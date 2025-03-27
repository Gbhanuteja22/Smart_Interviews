t=int(input())
for _ in range(t):
    myset=set()
    s=input()
    rep=[]
    for i in s:
        if i in myset:
            rep.append(i)  
        else:
            myset.add(i)
    val=len(s)+1
    for i in rep:
        val=min(val,s.index(i))
    if val==len(s)+1:
        print(".")
    else:
        print(s[val])
