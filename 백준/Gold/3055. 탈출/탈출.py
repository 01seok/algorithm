from collections import deque

def solve():

    R, C = map(int, input().split())
    field = [list(input()) for _ in range(R)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    water_q = deque()
    animal_q = deque()
    visited = [[False] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if field[r][c] == '*':
                water_q.append((r,c))
            elif field[r][c] == 'S':
                animal_q.append((r,c))
                visited[r][c] = True

    time = 0
    while animal_q:

        # 물 먼저 퍼짐
        for _ in range(len(water_q)):
            wr, wc = water_q.popleft()
            for d in range(4):
                nr, nc = wr + dr[d], wc + dc[d]
                if 0 <= nr < R and 0 <= nc < C:
                    if field[nr][nc] == '.':
                        field[nr][nc] = '*'
                        water_q.append((nr, nc))

        # 고슴도치 이동
        for _ in range(len(animal_q)):
            r, c = animal_q.popleft()
            if field[r][c] == 'D':
                print(time)
                return

            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < R and 0 <= nc < C:
                    if not visited[nr][nc] and (field[nr][nc] == '.' or field[nr][nc] == 'D'):
                        visited[nr][nc] = True
                        animal_q.append((nr, nc))
        time += 1

    print("KAKTUS")

solve()
