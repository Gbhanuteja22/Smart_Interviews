def hanoi(n,src,temp,dest):
    if n==0:
        return
    hanoi(n-1,src,dest,temp)
    print(f"Move {n} from {src} to {dest}")
    hanoi(n-1,temp,src,dest)
t=int(input())
for _ in range(t):
    n=int(input())
    moves=pow(2,n)-1
    print(moves)
    hanoi(n,"A","B","C")
