n=int(input())
arr=list(map(str,input().split()))
vowels=['A','E','I','O','U','a','e','i','o','u']
ans=[0]*(len(arr))
for i in range(len(arr)):
    if (arr[i][0] in vowels) and (arr[i][-1] in vowels):
        ans[i]=1
q=int(input())
for _ in range(q):
    u,v=map(int,input().split())
    count=0
    for i in range(u,v+1):
        if ans[i]==1:
            count+=1
    print(count)
