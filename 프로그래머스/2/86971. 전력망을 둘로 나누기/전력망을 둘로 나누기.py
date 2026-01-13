from collections import deque

def solution(n, wires):
    answer = float('inf')
    
    # 인접 리스트
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    # bfs
    # start node : 탐색 시작점
    # cut node : 끊어진 반대편
    def bfs(start_node, cut_node):
        cnt = 1
        visited = [False] * (n + 1)
        visited[start_node] = True
        
        q = deque([start_node])
        
        while q:
            cur = q.popleft()
            
            for next_node in graph[cur]:
                # 끊기로 한 노드면 pass
                if next_node == cut_node:
                    continue
                    
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node)
                    cnt += 1
        return cnt

    # 전선을 하나씩 끊어보며 완탐
    for v1, v2 in wires:
        # v1에서 출발, v2로는 가지 말기
        cnt = bfs(v1, v2)
        
        # 전력망의 차이 계산
        diff = abs(cnt - (n - cnt))
        answer = min(answer, diff)
        
    return answer