def balfunc(n,op,cc,res):
    if op==n and cc==n:
        print(res)
        return
    if op<n:
        balfunc(n,op+1,cc,res+'{');
    if cc<op:
        balfunc(n,op,cc+1,res+'}');
t=int(input())
for i in range(1,t+1):
    print(f"Test Case #{i}:")
    n=int(input())
    res=''
    balfunc(n,0,0,res)
