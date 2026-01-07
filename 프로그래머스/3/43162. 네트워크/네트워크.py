def solution(N, computers):

    # 방문 여부 기록
    visited = [False] * N
    network_cnt = 0

    # 연결된 모든 노드 dfs로 방문처리
    def dfs(node):
        visited[node] = True
        
        for next_node in range(N):
            # 자기 자신 아니고, 연결되어있고, 방문 안한 곳
            if node != next_node and computers[node][next_node] == 1 and not visited[next_node]:
                dfs(next_node)
    
    # 모든 컴퓨터를 순회
    for i in range(N):
        # 방문 안한 컴퓨터가 있으면 거긴 다른 곳들과 연결 안되어있으니 새 네트워크 시작점임
        if not visited[i]:
            dfs(i)
            network_cnt += 1
            

    return network_cnt