import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 북 동 남 서 (시계 방향 순서, 왼쪽 회전 = (d-1)%4)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 1
room[r][c] = 2  # 시작 칸 청소

while True:
    moved = False
    for _ in range(4):
        d = (d - 1) % 4  # 왼쪽 90도 회전
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            r, c = nr, nc
            room[r][c] = 2
            cnt += 1
            moved = True
            break

    if not moved:
        # 현재 방향 기준 후진 (반대 방향)
        br, bc = r - dr[d], c - dc[d]
        if room[br][bc] == 1:  # 후진 방향이 벽이면 종료
            break
        r, c = br, bc

print(cnt)