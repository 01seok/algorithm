from collections import deque

def solution(maps):
    
    # 맵의 행, 열 구하기
    N = len(maps)
    M = len(maps[0])
    
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1 , 1)
    
    # bfs 하기 위한 큐 세팅
    q = deque([(0, 0)])
    while q:
        r, c = q.popleft()
        
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            
            # 유효성 검사
            if 0 <= nr < N and 0 <= nc < M:
                if maps[nr][nc] == 1:
                    maps[nr][nc] = maps[r][c] + 1
                    q.append((nr, nc))
    
    answer = maps[N-1][M-1]
    if answer > 1:
        return answer
    else:
        return -1