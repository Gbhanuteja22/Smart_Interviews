for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    flag=0
    for p in range(n-2):
        d={}
        for q in range(p+1,n):
            if (k-(arr[p]+arr[q])) not in d:
                d[arr[q]]=1
            else:
                flag=1
                break
        if flag==1:
            break
    if flag==0:
        print("false")
    else:
        print("true")
