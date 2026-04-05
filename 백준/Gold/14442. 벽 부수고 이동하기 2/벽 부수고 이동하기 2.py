import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [input().strip() for _ in range(N)]

visited = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = True

q = deque()
q.append((0, 0, 0, 1))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = -1

while q:
    r, c, k, dist = q.popleft()

    if r == N - 1 and c == M - 1:
        ans = dist
        break

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if not (0 <= nr < N and 0 <= nc < M):
            continue

        if grid[nr][nc] == '0':
            if not visited[nr][nc][k]:
                visited[nr][nc][k] = True
                q.append((nr, nc, k, dist + 1))
        else:
            if k < K and not visited[nr][nc][k + 1]:
                visited[nr][nc][k + 1] = True
                q.append((nr, nc, k + 1, dist + 1))

print(ans)