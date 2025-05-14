import sys
input=sys.stdin.readline
t=int(input())
for k in range(1,t+1):
    print(f"Case {k}:")
    n=int(input())
    maxstk=[]
    stk=[]
    for _ in range(n):
        op=list(map(str,input().split()))
        if(op[0]=='A'):
            stk.append(int(op[1]))
            if not maxstk:
                maxstk.append(int(op[1]))
            else:
                maxstk.append(max(int(op[1]),maxstk[-1]))
        elif(op[0]=='R'):
            if(stk):
                stk.pop()
                maxstk.pop()
        else:
            if(maxstk):
                print(maxstk[-1])
            else:
                print("Empty")
