#Time Limited Exceeeded for LARGER TEST CASES
def ispow(x):
    return x>0 and (x&(x-1))==0
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if any(ispow(num) for num in arr):
        print("YES")
        continue
    andres=set()
    for num in arr:
        newres={num}
        for prev in andres:
            newres.add(prev&num)
        andres.update(newres)
        if(any(ispow(res) for res in andres)):
            print("YES")
            break
    else:
        print("NO")
#Time Limited Exceeeded for LARGER TEST CASES
