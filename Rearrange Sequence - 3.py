def func(arr,n):
    maxlen=0
    for i in range(n):
        freq={}
        minval=maxval=arr[i]
        for j in range(i,n):
            if arr[j]in freq:
                freq[arr[j]]+=1
            else:
                freq[arr[j]]=1
            minval=min(minval,arr[j])
            maxval=max(maxval,arr[j])
            if (maxval-minval<=j-i)and(len(freq)==maxval-minval+1):
                maxlen=max(maxlen,j-i+1)
    return maxlen
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(func(arr,n))
