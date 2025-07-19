import sys
from collections import deque

N_str = sys.stdin.readline()
N = int(N_str)
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    line = sys.stdin.readline()
    parts = line.split()
    u = int(parts[0])
    v = int(parts[1])
    graph[u].append(v)
    graph[v].append(u) # 양방향 연결

parents = [0] * (N + 1)

visited = [False] * (N + 1)

queue = deque()

queue.append(1)
visited[1] = True

while queue:
    current_node = queue.popleft()


    for neighbor in graph[current_node]:

        if not visited[neighbor]:
            parents[neighbor] = current_node
            visited[neighbor] = True
            queue.append(neighbor)


output_lines = []
for i in range(2, N + 1):
    output_lines.append(str(parents[i]))

sys.stdout.write('\n'.join(output_lines) + '\n')