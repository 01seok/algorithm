n=int(input())
a=[tuple(map(int,input().split())) for _ in range(n)]
a.sort()
for x,y in a:
    print(x,y)