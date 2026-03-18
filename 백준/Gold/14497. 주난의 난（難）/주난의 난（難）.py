'''
백준, 주난의 난
14479번 골드4
'''
import sys
from collections import deque

input = sys.stdin.readline
INF = float('inf')
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input(). split())
class_room = [list(input()) for _ in range(N)]


# 0 base index
start_r, start_c = x1-1, y1-1
end_r, end_c = x2-1, y2-1

dist = [[INF] * M for _ in range(N)]
dist[start_r][start_c] = 0

q = deque([(start_r, start_c)])


while q:
    now_r, now_c = q.popleft()
    if (now_r, now_c) == (end_r, end_c):
        break

    for d in range(4):
        nr, nc = now_r + dr[d], now_c + dc[d]
        if 0 <= nr < N and 0 <= nc < M:
            next_pos = class_room[nr][nc]
            if next_pos == '0':
                cost = 0
            else:
                cost = 1

            next_cost = dist[now_r][now_c] + cost

            if next_cost < dist[nr][nc]:
                dist[nr][nc] = next_cost

                if cost == 0:
                    q.appendleft((nr, nc))
                else:
                    q.append((nr,nc))

print(dist[end_r][end_c])