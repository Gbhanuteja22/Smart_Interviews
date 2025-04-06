for _ in range(int(input())):
    a,b=map(str,input().split())
    b=int(b)
    res=[]
    for i in a:
        val=chr((ord(i)-ord('a')+b)%26+ord('a'))
        print(val,end="")
    print()
