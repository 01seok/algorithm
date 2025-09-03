from collections import deque

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

baby_shark_pos = (0, 0)
for r in range(N):
    for c in range(N):
        if sea[r][c] == 9:
            baby_shark_pos = (r,c)
            sea[r][c] = 0
            break
    if baby_shark_pos != (0,0):
        break

shark_size = 2
shark_eat_cnt = 0
total_time = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start_r, start_c, cur_shark_size):
    q = deque([(start_r, start_c, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[start_r][start_c] = True

    can_eat_fishes = []

    while q:
        r, c, dist = q.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc]:
                    if sea[nr][nc] <= cur_shark_size:
                        visited[nr][nc] = True

                        if 0 < sea[nr][nc] < cur_shark_size:
                            can_eat_fishes.append((dist + 1, nr, nc))

                        else:
                            q.append((nr, nc, dist + 1))
    return can_eat_fishes

while True:
    # 먹을 수 있는 물고기 찾기, 매번 먹을 물고기 리스트
    can_eat_fishes = bfs(baby_shark_pos[0], baby_shark_pos[1], shark_size)

    if not can_eat_fishes:
        break

    can_eat_fishes.sort()   # 거리, 행, 열 순으로 정렬해서 문제 조건 맞추기 (거리 가까운 순, 행 작은 순, 열 작은 순)

    # 처음 먹을 물고기
    target_dist, target_r, target_c = can_eat_fishes[0]

    total_time += target_dist
    shark_eat_cnt += 1


    if shark_eat_cnt == shark_size:
        shark_size += 1
        shark_eat_cnt = 0

    baby_shark_pos = (target_r, target_c)
    sea[target_r][target_c] = 0

print(total_time)
