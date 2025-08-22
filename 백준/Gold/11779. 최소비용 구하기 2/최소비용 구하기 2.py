import sys
import heapq

INF = float('inf')
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
dist = [INF] * (N+1)
# 경로 역추적을 위한 리스트
reverse_path = [0] * (N+1)

for _ in range(M):
    u,v,w = map(int, input().split())
    graph[u].append((v, w))

start, goal = map(int, input().split())

pq = []
dist[start] = 0
heapq.heappush(pq, (0, start))

while pq:
    cur_dist, cur_node = heapq.heappop(pq)

    if dist[cur_node] < cur_dist:
        continue

    for next_node, weight in graph[cur_node]:
        new_dist = cur_dist + weight

        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            reverse_path[next_node] = cur_node
            heapq.heappush(pq, (new_dist, next_node))

print(dist[goal])

# 최소 비용 경로
path = []
current = goal
while current != 0:
    path.append(current)
    current = reverse_path[current]

path.reverse()

print(len(path))
print(*path)