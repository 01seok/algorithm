# 문제: 미로 탈출 (프로그래머스 Lv.2)
#
# 미로에는 출발 지점 'S', 레버 'L', 출구 'E', 벽 'X', 통로 'O'가 있다.
# 출발 지점에서 레버를 당긴 후 출구로 이동해야 한다.
# 이동 가능한 최소 시간(칸 수)을 반환하라. 불가능하면 -1 반환.
#
# 제한사항:
# - maps는 n x m 크기의 문자열 배열
# - 5 <= n, m <= 100
# - 이동은 상하좌우 4방향
#
# 입출력 예:
# maps = ["SOOOL", "XXXXL", "OOOOO", "OXXXX", "OOOOE"]
# result = 16
#
# maps = ["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]
# result = -1

from collections import deque
def solution(maps):
    maze = [list(row) for row in maps]
    N = len(maze)
    M = len(maze[0])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(N):
        for c in range(M):
            if maze[r][c] == "S":
                start_r, start_c = r, c

            if maze[r][c] == "L":
                lever_r, lever_c = r, c

            if maze[r][c] == "E":
                exit_r, exit_c = r, c

    def bfs(enter_r, enter_c, end_r, end_c):
        visited = [[False] * M for _ in range(N)]
        # 출발r, 출발c, 소요시간
        q = deque([(enter_r, enter_c, 0)])
        visited[enter_r][enter_c] = True

        while q:
            cur_r, cur_c, cur_time = q.popleft()

            if cur_r == end_r and cur_c == end_c:
                return cur_time

            for d in range(4):
                nr,nc = cur_r + dr[d], cur_c + dc[d]
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and maze[nr][nc] != "X":
                    q.append((nr, nc, cur_time +1))
                    visited[nr][nc] = True
        return -1


    dist1 = bfs(start_r, start_c, lever_r, lever_c)
    dist2 = bfs(lever_r, lever_c, exit_r, exit_c)
    if dist1 == -1 or dist2 == -1:
        return -1
    else:  
        return dist1 + dist2

