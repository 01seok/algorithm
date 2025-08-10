import heapq
import sys

N, D = map(int, sys.stdin.readline().split())
short_roads = []
for _ in range(N):
    start, end, length = map(int, sys.stdin.readline().split())
    if end <= D and end - start > length:
        short_roads.append((start, end, length))

short_roads.sort()
# 시작 ~ 도착지까지의 가중치 배열
dist = [i for i in range(D+1)]

cur_pos = 0
while cur_pos <= D:

    for start, end, length in short_roads:
        
        if start == cur_pos:
            next_dist = dist[cur_pos] + length
            if next_dist < dist[end]:
                dist[end] = next_dist
    
    # 지름길 없이 1km만 이동
    if cur_pos + 1 <= D:
        if dist[cur_pos] + 1 < dist[cur_pos + 1]:
            dist[cur_pos + 1] = dist[cur_pos] + 1
    
    cur_pos += 1

print(dist[D])