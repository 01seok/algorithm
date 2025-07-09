import math

def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):

    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return

    if root_x < root_y:
        parents[root_y] = root_x

    else:
        parents[root_x] = root_y
    
N = int(input())
stars = []
for _ in range(N):
    a, b = map(float, input().split())
    stars.append((a, b))

edges = []
for i in range(N):
    for j in range(i+1, N):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        
        distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        edges.append((distance,i, j))   # 가중치, 별1, 별2

edges.sort()

parents = [i for i in range(N+1)]

cnt = 0
weight = 0

for w,u,v in edges:
    if find_set(u) != find_set(v):
        union(u, v)
        cnt += 1
        weight += w
    
    if cnt == N-1:
        break
print(f'{weight:.2f}')