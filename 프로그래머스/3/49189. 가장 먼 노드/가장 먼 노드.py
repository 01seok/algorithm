from collections import deque
def solution(N, edge):

    # 입력 받을 그래프 초기화, 1번부터니까 N+1
    graph = [[] for _ in range(N+1)]

    # 양방향 그래프 간선 정보 입력
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # 거리 측정 위한 배열
    dist = [-1] * (N+1)

    # 시작 노드 1번
    dist[1] = 0

    q = deque([1])
    while q:
        cur_node = q.popleft()

        # 현재 노드랑 연결된 모든 노드 확인하기
        for next_node in graph[cur_node]:

            # 아직 안 간 곳이면 거리 갱신해주기 (not visited)
            if dist[next_node] == -1:
                dist[next_node] = dist[cur_node] + 1
                q.append(next_node)
                
    # 제일 먼 곳 찾기
    max_dist = max(dist)
    
    
    return dist.count(max_dist)