from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])

    answer = [0] * m
    visited = [[False] * m for _ in range(n)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True

                oil_count = 0
                columns = set()

                while q:
                    r, c = q.popleft()
                    oil_count += 1
                    columns.add(c)

                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]

                        if 0 <= nr < n and 0 <= nc < m:
                            if land[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr, nc))

                for col in columns:
                    answer[col] += oil_count

    return max(answer)