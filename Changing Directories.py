t=int(input())
for _ in range(t):
    n=int(input())
    stk=[]
    for _ in range(n):
        ip=input().strip()
        if(ip=="pwd"):
            print("/",end="")
            if stk:
                for i in stk:
                    print(i+"/",end="")
            print()
        if(ip.startswith("cd ")):
            path=ip[3:]
            if(path.startswith("/")):
                stk=[]
                path=path[1:]
            dirs=path.strip("/").split("/")
            for d in dirs:
                if d=="..":
                    if stk:
                        stk.pop()
                elif d:
                    stk.append(d)
    print()
