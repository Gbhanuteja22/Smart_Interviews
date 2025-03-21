for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    d={}
    flag=0
    for i in arr:
        if k-i not in d:
            d[i]=1
        else:
            flag=1
            break
    if flag==1:
        print("True")
    else:
        print("False")
