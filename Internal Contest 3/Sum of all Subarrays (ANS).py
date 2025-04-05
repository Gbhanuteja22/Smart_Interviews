# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))

    sum = 0
    for i in range(n):
        sum += l[i]*(i-1)*(n+1)
    print(l)
