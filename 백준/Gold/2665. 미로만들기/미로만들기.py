import sys
import heapq

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

input = sys.stdin.readline
N = int(input())
rooms = [list(map(int, input().strip())) for _ in range(N)]
INF = float('inf')
cost = [[INF] * N for _ in range(N)]

def djikstra():
    pq = []
    cost[0][0] = 0  # 출발지는 항상 비용 0
    heapq.heappush(pq, (0, 0, 0))   # cost, r, c

    while pq:
        cur_cost, cur_r, cur_c = heapq.heappop(pq)

        if cur_cost > cost[cur_r][cur_c]:
            continue

        if (cur_r, cur_c) == (N-1, N-1):
            break

        for d in range(4):
            nr, nc = cur_r + dr[d], cur_c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if rooms[nr][nc] == 0:
                    move_cost = 1
                else:
                    move_cost = 0
                
                new_cost = cur_cost + move_cost

                if new_cost < cost[nr][nc]:
                    cost[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))
                
        
djikstra()
print(cost[N-1][N-1])