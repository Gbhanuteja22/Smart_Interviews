t=int(input())
for _ in range(t):
    str1=input()
    str2=input()
    q=int(input())
    for p in range(q):
        i,j,k,l=map(int,input().split())
        s1=str1[i:j+1]
        s2=str2[k:l+1]
        if (s1==(s2)):
            print("Yes")
        else:
            print("No")
