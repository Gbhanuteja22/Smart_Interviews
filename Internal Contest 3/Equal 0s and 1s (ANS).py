for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=0

    #replacing all 0's with -1
    for i in range(n):
        if arr[i]==0:
            arr[i]=-1

    #Creating prefix array
    pre=[0]*n
    pre[0]=arr[0]
    for i in range(1,n):
        pre[i]=arr[i]+pre[i-1]
    #Finding the answer
    hm={0:-1}
    for i in range(n):
        if pre[i] not in hm:
            hm[pre[i]]=i
        else:
            ans=max(ans,i-hm[pre[i]])
    print(ans)
