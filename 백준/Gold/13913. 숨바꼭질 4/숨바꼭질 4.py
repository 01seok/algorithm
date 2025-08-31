from collections import deque

N, K = map(int, input().split())


if N >= K:
    print(N-K)
    print(*range(N, K-1, -1))
    
else:
    visited = [False] * 100001
    q = deque()
    q.append((N, 0, [N]))
    visited[N] = True
    
    while q:
        cur_pos, cur_time,path = q.popleft()
    
        if cur_pos == K:
            print(cur_time)
            print(*path)
            break
    
        for next_pos in [cur_pos-1, cur_pos+1, cur_pos *2]:
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                q.append((next_pos, cur_time+1, path + [next_pos]))
