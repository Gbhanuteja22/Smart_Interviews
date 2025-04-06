def lps(s,n):
    maxlen=0
    def check(left,right):
        while((left>=0 and right<n) and(s[left]==s[right])):
            left-=1
            right+=1
        return right-left-1
    for i in range(len(s)):
        odd=check(i,i)
        eve=check(i,i+1)
        currlen=max(odd,eve)
        maxlen=max(maxlen,currlen)
    return maxlen
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    print(lps(s,n))
