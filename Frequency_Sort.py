from collections import Counter
def freq(arr):
    freq=Counter(arr)
    sortedarr=sorted(arr,key=lambda x:(freq[x],x))
    for i in sortedarr:
        print(i,end=" ")
    print()
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    freq(arr)
