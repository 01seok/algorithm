from collections import deque

def solution(m, n, h, w, drops):
    INF = len(drops) + 1

    # grid[r][c] = 해당 칸이 몇 번째 빗방울에 젖는지
    # 비가 안 오는 칸은 INF
    grid = [[INF] * n for _ in range(m)]

    for time, (r, c) in enumerate(drops, 1):
        grid[r][c] = time

    # 1단계: 각 행마다 가로 w칸 구간의 최솟값 구하기
    row_min = []

    for r in range(m):
        dq = deque()
        temp = []

        for c in range(n):
            while dq and grid[r][dq[-1]] >= grid[r][c]:
                dq.pop()

            dq.append(c)

            if dq[0] <= c - w:
                dq.popleft()

            if c >= w - 1:
                temp.append(grid[r][dq[0]])

        row_min.append(temp)

    # 2단계: row_min에서 세로 h칸 구간의 최솟값 구하기
    # 즉, 각 h x w 직사각형 내부의 최솟값을 구함
    best = -1
    answer = [0, 0]

    col_count = n - w + 1

    for c in range(col_count):
        dq = deque()

        for r in range(m):
            while dq and row_min[dq[-1]][c] >= row_min[r][c]:
                dq.pop()

            dq.append(r)

            if dq[0] <= r - h:
                dq.popleft()

            if r >= h - 1:
                top = r - h + 1
                current = row_min[dq[0]][c]

                # current가 클수록 더 늦게 비를 맞음
                # 같다면 더 위쪽, 더 왼쪽 좌표 선택
                if current > best or (current == best and [top, c] < answer):
                    best = current
                    answer = [top, c]

    return answer