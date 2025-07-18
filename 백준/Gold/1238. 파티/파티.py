import sys
import heapq
input = sys.stdin.readline
INF = float('inf')
N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)] # 각 각의 마을에서 파티장 까지 비용, 도착노드 들어갈 리스트
rev_graph = [[] for _ in range(N+1)]    # 파티장에서 각 자 마을까지

for _ in range(M):
    u, v, w = map(int, input().split())
    # 파티장에서 각자 집으로 가는건 정방향 그래프 한 번만 돌리면 되고, 각자 집에서 파티장으로 가는 최단거리는 역방향 한 번만 돌리면 됨
    graph[v].append((w, u)) # 집 -> 파티장, 역방향 간선 저장
    rev_graph[u].append((w, v))
    
def djikstra(start, lst):
    dist = [INF] * (N+1)
    dist[start] = 0
    pq = [(0, start)]   # cost, start
    
    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if cur_cost > dist[cur_node]:
            continue
        for next_cost, next_node in lst[cur_node]:
            new_cost = cur_cost + next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
    return dist

to_party = djikstra(X, graph)
to_home = djikstra(X, rev_graph)

max_time = 0
for i in range(1, N+1):
    now_person_time = to_party[i] + to_home[i]
    if now_person_time > max_time:
        max_time = now_person_time
print(max_time)