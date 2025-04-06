t=int(input())
for _ in range(t):
    a,b=map(str,input().split())
    for i in b:
        if i not in a:
            print(i,end="")
    print()
