N =int(input())
apt = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
ans = []

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c):
    stack = [(r,c)]
    cnt = 0

    while stack:
        cur_r, cur_c = stack.pop()

        if visited[cur_r][cur_c]:
            continue

        visited[cur_r][cur_c] = True
        cnt += 1

        for d in range(4):
            nr, nc = cur_r + dr[d], cur_c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if apt[nr][nc] == 1 and not visited[nr][nc]:
                    stack.append((nr, nc))
    return cnt

for r in range(N):
    for c in range(N):
        if apt[r][c] == 1 and not visited[r][c]:
            ans.append(dfs(r,c))

ans.sort()
print(len(ans))
for i in ans:
    print(i)