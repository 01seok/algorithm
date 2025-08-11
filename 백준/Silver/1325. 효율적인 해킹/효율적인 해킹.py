import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

def bfs(start):
    visited = [False] * (N+1)
    visited[start] = True
    q = deque([start])
    cnt = 1
    
    while q:
        cur_node = q.popleft()
        for next in graph[cur_node]:
            if not visited[next]:
                visited[next] = True
                cnt += 1
                q.append(next)
    return cnt

max_cnt = 0
result = []

for i in range(1, N+1):
    cnt = bfs(i)
    
    if cnt > max_cnt:
        max_cnt = cnt
        result = [i]
    elif cnt == max_cnt:
        result.append(i)
        
print(*result)