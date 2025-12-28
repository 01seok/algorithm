import sys
from collections import deque

input = sys.stdin.readline
dr = (-1, 1, 0, 0)
dc = (0, 0, -1 , 1)

N, M = map(int, input().split())

# 전쟁터 지도
field = [list(input()) for _ in range(M)]

# visited
visited = [[False] * N for _ in range(M)]

# 정답 저장 변수
white_pow = 0
blue_pow = 0

for r in range(M):
    for c in range(N):
        # 아직 확인하지 않은 병사라면
        if not visited[r][c]:
            # 지금 병사 색깔 저장
            cur_color = field[r][c]
            
            # bfs 큐 생성
            q = deque([(r,c)])
            visited[r][c] = True
            
            # 현재 병사 카운트
            cur_color_cnt = 1
            
            while q:
                cur_r, cur_c = q.popleft()
                
                for d in range(4):
                    nr, nc = cur_r + dr[d], cur_c + dc[d]
                    
                    if 0 <= nr < M and 0 <= nc < N:
                        if not visited[nr][nc] and field[nr][nc] == cur_color:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                            cur_color_cnt += 1
            
            if cur_color == 'W':
                white_pow += cur_color_cnt ** 2
                
            else:
                blue_pow += cur_color_cnt ** 2

print(white_pow, blue_pow)