t=int(input())
for _ in range(t):
    n=int(input())
    if(n&(n-1)==0):
        print('True')
    else:
        print('False')
