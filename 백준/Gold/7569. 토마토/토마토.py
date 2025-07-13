from collections import deque

M, N, H = map(int, input().split()) # 가로, 세로, 높이

# 3차원으로 구성되어있는 토마토 상자
box = []
# visited 배열의 역할을 하면서, 며칠만에 모두 익게되는지 기록해둘 3차원 배열
days = [[[-1 for _ in range(M)] for _ in range(N)]for _ in range(H)]
q = deque()

for i in range(H):
    floor = []  # 2차원 배열, 한 층의 토마토 구조(임시 사용)
    for j in range(N):
        floor.append(list(map(int, input().split())))
    box.append(floor)   # 한 층 입력 끝날 때 마다 3차원 토마토 상자에 넣어주기

# 처음부터 익어있는 토마토 찾아 큐에 넣어두기(bfs 시작할 곳들)
for i in range(H):
    for r in range(N):
        for c in range(M):
            if box[i][r][c] == 1:
                q.append((i,r,c))
                days[i][r][c] = 0   # 처음부터 익어있던 토마토는 0일 + 방문처리

dr = [-1, 1, 0, 0, 0, 0]    # 상하
dc = [0, 0, -1, 1, 0, 0]    # 좌우
dh = [0, 0, 0, 0, 1, -1]    # 앞뒤

while q:
    cur_h, cur_r, cur_c = q.popleft()

    for d in range(6):
        nh, nr, nc = cur_h +dh[d], cur_r + dr[d], cur_c + dc[d]
        if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M:
            # 아직 방문하지 않았고, 익지않은 토마토일 때
            if days[nh][nr][nc] == -1 and box[nh][nr][nc] == 0:
                days[nh][nr][nc] = days[cur_h][cur_r][cur_c] + 1
                q.append((nh,nr,nc))
ans_day = 0
flag = False    # 다 익을 수 없는 경우 탈출하기 위한 플래그 변수

for h in range(H):
    for r in range(N):
        for c in range(M):
            if box[h][r][c] == 0 and days[h][r][c] == -1:
                flag = True
                break
            ans_day = max(ans_day, days[h][r][c])
        if flag:
            break

if flag:
    print(-1)
else:
    print(ans_day)