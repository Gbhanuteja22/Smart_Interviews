t=int(input())
for _ in range(t):
    s,m=map(str,input().split())
    if(sorted(s)==sorted(m)):
        print("True")
    else:
        print("False")
