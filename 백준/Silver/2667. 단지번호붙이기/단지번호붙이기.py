N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
result = []

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    stack = [(r, c)]
    count = 0

    while stack:
        cr, cc = stack.pop()
        if visited[cr][cc]:
            continue
        visited[cr][cc] = True
        count += 1

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and graph[nr][nc] == 1:
                    stack.append((nr, nc))

    return count

for r in range(N):
    for c in range(N):
        if graph[r][c] == 1 and not visited[r][c]:
            result.append(dfs(r, c))

result.sort()
print(len(result))
for x in result:
    print(x)