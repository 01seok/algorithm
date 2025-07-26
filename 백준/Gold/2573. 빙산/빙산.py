'''

1. 빙산 녹는 함수
원본 맵 훼손 하지않는 복사 맵(copy_ice_map)에서 진행
빙산 높이 최소 0 보장해주기

2. 빙산 덩어리 개수 세는 함수(bfs)
bfs 끊길 때 마다 덩어리 1개 추가

3. while문 안에서 종료조건 채울 때 까지 반복
빙산 녹는 함수 실행해서 모든 빙산 녹았는지 확인하기
빙산 덩어리 개수 세는 함수 돌려서 2 덩어리 나왔는지 확인하기

'''

import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
origin_ice_map = []
for _ in range(N):
    origin_ice_map.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

year = 0

# 빙산 녹이는 함수
def melt_ice(cur_ice_map):
    copy_ice_map = [row[:] for row in cur_ice_map] # 복사 맵

    for r in range(N):
        for c in range(M):
            if cur_ice_map[r][c] > 0:
                sea_cnt = 0

                for d in range(4):
                    nr, nc = r +dr[d], c + dc[d]

                    # 현재 빙산 옆이 바다면 sea_cnt + 1
                    if 0 <= nr < N and 0 <= nc < M and cur_ice_map[nr][nc] == 0:
                        sea_cnt += 1
                # 복사 맵에 체크해주기 (원본 맵 훼손 x)
                copy_ice_map[r][c] = max(0, cur_ice_map[r][c] - sea_cnt)
    return copy_ice_map

# 빙산 덩어리 세는 함수
def cnt_iceberg(cur_ice_map):
    visited = [[False] * M for _ in range(N)]
    icebergs = 0

    for r in range(N):
        for c in range(M):
            if cur_ice_map[r][c] > 0 and not visited[r][c]: # 방문x, 빙산인 경우에만
                icebergs += 1


                q = deque([(r, c)])
                visited[r][c] = True

                while q:
                    cur_r, cur_c = q.popleft()

                    for d in range(4):
                        nr, nc = cur_r + dr[d], cur_c + dc[d]

                        if 0 <= nr < N and 0 <= nc < M and cur_ice_map[nr][nc] > 0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))
    return icebergs


while True:
    year += 1
    origin_ice_map = melt_ice(origin_ice_map)

    # 2덩어리 되기 전에 빙산 다 녹았는지 확인
    ice_height = 0
    for r in range(N):
        ice_height += sum(origin_ice_map[r])
    if ice_height == 0:
        print(0)
        break

    # 1년 마다 얼음 덩어리 세서 2 덩어리면 year 출력하기
    icebergs = cnt_iceberg(origin_ice_map)
    if icebergs >= 2:
        print(year)
        break