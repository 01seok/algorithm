import sys
input=sys.stdin.readline

n,m=map(int,input().split())
name=[0]*(n+1)
dic={}
for i in range(1,n+1):
    s=input().strip()
    name[i]=s
    dic[s]=i
for _ in range(m):
    q=input().strip()
    if q.isdigit():
        print(name[int(q)])
    else:
        print(dic[q])