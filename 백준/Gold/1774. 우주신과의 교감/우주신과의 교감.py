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
        return False

    if root_x < root_y:
        parents[root_y] = root_x

    else:
        parents[root_x] = root_y

    return True

def distance(x1, x2):
    return math.sqrt((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2)

N, M = map(int, input().split())
gods = []
for _ in range(N):
    x, y = map(int, input().split())
    gods.append((x,y))

parents = [i for i in range(N+1)]
edges = []
for i in range(N):
    for j in range(i+1, N):
        dist = distance(gods[i], gods[j])
        edges.append((dist,i+1, j+1))
edges.sort()

cnt = 0
total = 0

for _ in range(M):  # 이미 연결된 간선의 정보
    u, v = map(int, input().split())
    if find_set(u) != find_set(v):
        cnt += 1
        union(u, v)

for w, a, b in edges:
    if cnt == N-1:
        break

    if find_set(a) != find_set(b):
        union(a, b)
        cnt += 1
        total += w

print(f'{total:.2f}')