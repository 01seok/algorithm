import sys
from collections import deque

N, M = map(int, input().split())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

visited = [[False] * M for _ in range(N)]
print_area_cnt = 0  # 그림 영역 개수
max_area = 0        # 최대 그림 넓이



for r in range(N):
    for c in range(M):
        if paper[r][c] == 1 and not visited[r][c]:
            cur_area = 1 # 그림의 최대 영역
            print_area_cnt += 1  # 그림 영역 개수
            visited[r][c] = True
            q = deque([(r,c)])

            while q:
                cur_r, cur_c = q.popleft()
                for d in range(4):
                    nr, nc = cur_r + dr[d], cur_c + dc[d]
                    if 0 <= nr < N and 0 <= nc < M and paper[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr,nc))
                        cur_area += 1
            max_area = max(max_area, cur_area)

print(print_area_cnt)
print(max_area)