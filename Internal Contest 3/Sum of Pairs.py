def pair(N,arr,k):
    arr.sort()
    p1,p2 = 0,N-1
    while p1 < p2:
        curr_sum = arr[p1] + arr[p2]
        if curr_sum == k:
            return True
        elif curr_sum > k:
            p2 -= 1
        else:
            p1 += 1
    return False

for _ in range(int(input())):
    N,k = map(int,input().split())
    arr = list(map(int,input().split()))
    print(pair(N,arr,k))
