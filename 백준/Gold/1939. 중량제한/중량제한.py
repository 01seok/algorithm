import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
INF = 1000000001

adj_lst = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int, input().split())
    adj_lst[a].append((b, c))
    adj_lst[b].append((a, c))

start, end = map(int, input().split())
dist = [-1] * (N+1)

pq = [] # 최대 힙
dist[start] = INF   # 시작점의 감당할 수 있는 무게는 INF로 설정, 무조건 시작해야하니
heapq.heappush(pq, (-INF, start))   # 최대 힙에 유지 가능 중량(heapq는 최소 힙이니 INF가 나올 수 있게 음수 부호, 현재 노드 번호 넣고 시작

while pq:
    cur_limit, cur_node = heapq.heappop(pq) # 현재 가질 수 있는 최대 유지 가능 중량, 현재 노드
    cur_limit = -cur_limit  # 음수 부호 달아서 원래 값으로 복구

    if cur_limit < dist[cur_node]:
        continue

    for next_node, next_limit in adj_lst[cur_node]:
        new_limit = min(cur_limit, next_limit)
        if new_limit > dist[next_node]:
            dist[next_node] = new_limit
            heapq.heappush(pq, (-new_limit, next_node))

print(dist[end])