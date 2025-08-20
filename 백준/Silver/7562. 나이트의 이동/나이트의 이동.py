import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, 2, 1, -1, -2]

def bfs():
    L = int(input())
    cur_r, cur_c = map(int, input().split())
    goal_r, goal_c = map(int, input().split())

    if cur_r == goal_r and cur_c == goal_c:
        print(0)
        return

    visited = [[False] * L for _ in range(L)]
    q = deque()
    q.append((cur_r, cur_c, 0))
    visited[cur_r][cur_c] = True

    while q:
        r, c, count = q.popleft()

        for d in range(8):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < L and 0 <= nc < L and not visited[nr][nc]:
                if nr == goal_r and nc == goal_c:
                    print(count + 1)
                    return
                visited[nr][nc] = True
                q.append((nr, nc, count + 1))

T = int(input())
for _ in range(T):
    bfs()