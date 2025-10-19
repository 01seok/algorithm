import sys
input=sys.stdin.readline
def check(s,l,r):
    if l>=r:
        return 1,1
    if s[l]!=s[r]:
        return 0,1
    res,c=check(s,l+1,r-1)
    return res,c+1

t=int(input())
for _ in range(t):
    s=input().strip()
    r,c=check(s,0,len(s)-1)
    print(r)
    print(c)