for _ in range(int(input())):
    n=int(input())
    res=0
    for i in range(0,32,2):
        ni=(n>>i)&1
        nj=(n>>i+1)&1
        res|=(ni<<i+1)|(nj<<i)
    print(res)
