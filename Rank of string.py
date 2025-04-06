from math import factorial
def find(s):
    n=len(s)
    rank=1
    fact=[1]*(n+1)
    for i in range(1,n+1):
        fact[i]=fact[i-1]*(i)
    for i in range(n):
        count=sum(1 for j in range(i+1,n) if s[j]<s[i])
        rank+=(fact[n-i-1]*count)
    return rank
t=int(input())
for _ in range(t):
    s=input()
    print(find(s))
