from itertools import product
from collections import deque

def solution(n, infection, edges, k):
    graph = [[] for _ in range(4)]

    for x, y, t in edges:
        graph[t].append((x - 1, y - 1))

    connected = [[0] * n for _ in range(4)]

    for t in range(1, 4):
        adj = [[] for _ in range(n)]

        for x, y in graph[t]:
            adj[x].append(y)
            adj[y].append(x)

        visited = [False] * n

        for start in range(n):
            if visited[start]:
                continue

            q = deque([start])
            visited[start] = True
            nodes = []
            mask = 0

            while q:
                cur = q.popleft()
                nodes.append(cur)
                mask |= 1 << cur

                for nxt in adj[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)

            for node in nodes:
                connected[t][node] = mask

    answer = 1
    start_mask = 1 << (infection - 1)

    for order in product([1, 2, 3], repeat=k):
        infected = start_mask

        for pipe_type in order:
            next_infected = infected

            for node in range(n):
                if infected & (1 << node):
                    next_infected |= connected[pipe_type][node]

            infected = next_infected

        answer = max(answer, bin(infected).count("1"))

    return answer