import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())
paper = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(y1, y2):
        for c in range(x1, x2):
            paper[r][c] = 1 # 직사각형이 그려진 구역은 1로 채워두기

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

area_sizes = []
num_of_area = 0

for r in range(M):
    for c in range(N):
        if paper[r][c] == 0:
            num_of_area += 1
            cur_area_size = 0

            q = deque([(r, c)])
            paper[r][c] = 1 # 한번 체크한 구역은 1로 처리 (visited)
            cur_area_size += 1

            while q:
                cur_r, cur_c = q.popleft()

                for d in range(4):
                    nr, nc = cur_r + dr[d], cur_c + dc[d]
                    if 0 <= nr < M and 0 <= nc < N and paper[nr][nc] == 0:
                        paper[nr][nc] = 1
                        q.append((nr, nc))
                        cur_area_size += 1
            area_sizes.append(cur_area_size)    # 한 영역 다 세어봤으니 크기 넣어주기

area_sizes.sort()

print(num_of_area)
print(*area_sizes)