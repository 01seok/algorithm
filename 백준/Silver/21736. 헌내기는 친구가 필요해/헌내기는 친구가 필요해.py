import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
campus = [list(sys.stdin.readline()) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cnt = 0

visited = [[False] * M for _ in range(N)]

start_r, start_c = -1, -1
for r in range(N):
    for c in range(M):
        if campus[r][c] == 'I':
            start_r, start_c = r, c
            break
    if start_r != -1:
        break

def bfs(r, c):

    global cnt

    q = deque([(r, c)])
    visited[r][c] = True

    while q:
        cur_r, cur_c = q.popleft()

        if campus[cur_r][cur_c] == 'P':
            cnt += 1

        for d in range(4):
            nr, nc = cur_r + dr[d], cur_c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and campus[nr][nc] != 'X':
                visited[nr][nc] = True
                q.append((nr, nc))


bfs(start_r, start_c)

if cnt == 0:
    print('TT')
else:
    print(cnt)