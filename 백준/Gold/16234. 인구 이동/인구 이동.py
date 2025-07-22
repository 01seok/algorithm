import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
world = []
for _ in range(N):
    world.append(list(map(int, input().split())))

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(start_r, start_c, visited):
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = True

    union = [(start_r, start_c)]
    total_population = world[start_r][start_c]

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                pop_gap = abs(world[r][c] - world[nr][nc])
                if L <= pop_gap <= R:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    union.append((nr, nc))
                    total_population += world[nr][nc]
    return union, total_population

days = 0

while True:
    visited = [[False] * N for _ in range(N)]
    is_move = False # 인구 이동 여부

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                union, total = bfs(r,c,visited)

                if len(union) > 1:
                    is_move = True
                    new_population = total // len(union)
                    for i, j in union:
                        world[i][j] = new_population
    if not is_move:
        break

    days += 1

print(days)