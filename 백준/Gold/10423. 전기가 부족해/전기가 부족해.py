import sys
input = sys.stdin.readline

def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):

    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return

    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y

N,M,K = map(int, input().split())   # 노드 수, 간선 수, 발전소 수
plants = list(map(int, input().split()))    # 발전소가 있는 위치

edges = []
for _ in range(M):
    u,v,w = map(int, input().split())
    edges.append((w,u,v))   # cost, node1, node2
edges.sort()
parents = [i for i in range(N+1)]

if K > 1:
    first_plant = plants[0]
    for i in range(1, K):
        union(first_plant, plants[i])

total = 0
cnt = 0

for w,u,v in edges:
    if find_set(u) != find_set(v):
        union(u, v)
        total += w
        cnt += 1

        if cnt == N-1:
            break
print(total)