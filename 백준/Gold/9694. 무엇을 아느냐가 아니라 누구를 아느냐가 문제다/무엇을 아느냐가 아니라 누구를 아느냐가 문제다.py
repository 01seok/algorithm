import heapq

def dijkstra(graph, start, end, M):
    INF = float('inf')
    dist = [INF] * M

    # 이전 노드가 어디였는지 확인하기 위한 배열
    # 경로 역추적용
    prev = [-1] * M
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cost, u = heapq.heappop(pq)

        # 더 작은 경우 있으면 패스
        if cost > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    # 다 돌았는데 닿을 수 없다면
    if dist[end] == INF:
        return None

    # 경로 역추적
    path = []
    node = end
    # -1이라면 끝난 것
    while node != -1:
        path.append(node)
        node = prev[node]

    path.reverse()
    return path

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(M)]

    for _ in range(N):
        x,y,z = map(int, input().split())
        graph[x].append((y,z))
        graph[y].append((x,z))

    path = dijkstra(graph, 0, M-1, M)

    if path is None:
        print(f"Case #{tc}: -1")
    else:
        print(f"Case #{tc}:", *path)