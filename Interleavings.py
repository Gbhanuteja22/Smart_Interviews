def func(a,b,res,inter):
    if not a and not b:
        inter.append(res)
        return
    if a:
        func(a[1:],b,res+a[0],inter)
    if b:
        func(a,b[1:],res+b[0],inter)
t=int(input())
for k in range(1,t+1):
    a,b=map(str,input().split())
    inter=[]
    func(a,b,"",inter)
    inter.sort()
    print(f"Case #{k}:")
    for s in inter:
        print(s)
