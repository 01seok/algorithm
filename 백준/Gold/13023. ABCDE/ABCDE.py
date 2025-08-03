import sys

def dfs(cur_node, level, visited, adj_lst):
    if level == 4:
        return True

    visited[cur_node] = True

    for next_node in adj_lst[cur_node]:
        if not visited[next_node]:
            if dfs(next_node, level + 1, visited, adj_lst):
                return True

    visited[cur_node] = False
    return False

N, M = map(int, sys.stdin.readline().split())

adj_lst = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

is_answer = False
for i in range(N):
    visited = [False] * N
    if dfs(i, 0, visited, adj_lst):
        is_answer = True
        break

if is_answer:
    print(1)
else:
    print(0)