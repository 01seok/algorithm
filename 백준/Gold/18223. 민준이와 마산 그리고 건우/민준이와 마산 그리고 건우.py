import heapq
INF = float('inf')

V, E, P = map(int, input().split())
adj_lst = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adj_lst[a].append((c, b))
    adj_lst[b].append((c, a))

# 건우 만난 버전 = True, 안 만난 버전 False
dist = [[INF, INF] for _ in range(V+1)]

pq = []

# 시작점이 건우 위치인 경우
if P == 1:
    dist[1][True] = 0
    heapq.heappush(pq, (0, 1, True))
else:
    dist[1][False] = 0
    heapq.heappush(pq, (0, 1, False))

while pq:
    cur_dist, cur_pos, 건우만남 = heapq.heappop(pq)

    if dist[cur_pos][건우만남] < cur_dist:
        continue

    for next_cost, next_pos in adj_lst[cur_pos]:
        next_dist = cur_dist + next_cost

        if next_dist < dist[next_pos][건우만남]:
            dist[next_pos][건우만남] = next_dist
            heapq.heappush(pq, (next_dist, next_pos, 건우만남))

        if not 건우만남 and next_pos == P:
            if next_dist < dist[next_pos][True]:
                dist[next_pos][True] = next_dist
                heapq.heappush(pq, (next_dist, next_pos, True))


if dist[V][True] <= dist[V][False]:
    print("SAVE HIM")
else:
    print("GOOD BYE")