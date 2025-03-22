def myfunc(arr,k):
    low=0
    high=n-1
    ans=-2147483648
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==k):
            return arr[mid]
        elif (arr[mid]<k):
            ans=arr[mid]
…    print(myfunc(arr,k))
