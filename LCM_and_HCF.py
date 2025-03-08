def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)
def lcm(a,b):
    return abs(a*b)//hcf(a,b)
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    print(lcm(a,b),end=" ")
    print(hcf(a,b))