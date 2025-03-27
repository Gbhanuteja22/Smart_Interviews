t=int(input())
for _ in range(t):
    s=input()
    myset=set()
    flag=0
    for i in s:
        if i not in myset:
            myset.add(i)
        else:
            flag=1
            print(i)
            break
    if flag==0:
        print(".")
