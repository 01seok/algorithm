from collections import deque

N, M = map(int, input().split())
move = [i for i in range(101)]
for _ in range(N + M):
    a, b = map(int, input().split())
    move[a] = b

visited = [False] * 101
q = deque()
q.append((1, 0))
visited[1] = True

while q:
    cur_pos, cnt = q.popleft()

    if cur_pos == 100:
        print(cnt)
        break

    for next_move in range(1, 7):
        next_pos = cur_pos + next_move
        if next_pos <= 100 and not visited[move[next_pos]]:
            visited[move[next_pos]] = True
            q.append((move[next_pos], cnt + 1))
