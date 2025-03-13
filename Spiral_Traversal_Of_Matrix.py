def spiral(arr):
    res=[]
    top,bottom=0,len(arr)-1
    left,right=0,len(arr[0])-1
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            res.append(arr[top][i])
        top+=1
        for i in range(top,bottom+1):
            res.append(arr[i][right])
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                res.append(arr[bottom][i])
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                res.append(arr[i][left])
            left+=1
    return res
t=int(input())
for _ in range(t):
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    res=spiral(arr)
    for i in res:
        print(i,end=" ")
    print()
