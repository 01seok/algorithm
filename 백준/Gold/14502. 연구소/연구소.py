import sys
from collections import deque
from itertools import combinations

# 대량 입력 처리 속도를 위해 sys.stdin.read() 사용
input_data = sys.stdin.read().split()
idx = 0

N = int(input_data[idx]); idx += 1
M = int(input_data[idx]); idx += 1

original_map = []
for r in range(N):
    row = []
    for c in range(M):
        row.append(int(input_data[idx])); idx += 1
    original_map.append(row)

# 상하좌우 이동 방향 (BFS 확산용)
DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]

# 빈 칸(0)과 바이러스(2) 위치 수집
empty_cells = []
virus_cells = []
for r in range(N):
    for c in range(M):
        if original_map[r][c] == 0:
            empty_cells.append((r, c))
        elif original_map[r][c] == 2:
            virus_cells.append((r, c))


def bfs_simulate(grid):
    queue = deque(virus_cells)
    # 격자 복사: 시뮬레이션마다 독립적인 상태 유지를 위해
    temp = [row[:] for row in grid]

    while queue:
        r, c = queue.popleft()
        for dr, dc in zip(DR, DC):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and temp[nr][nc] == 0:
                temp[nr][nc] = 2
                queue.append((nr, nc))

    # 바이러스 확산 후 안전 영역(0) 개수 반환
    return sum(cell == 0 for row in temp for cell in row)


max_safe = 0

# 빈 칸 중 3개를 골라 벽을 세우는 모든 조합 탐색
for wall_positions in combinations(empty_cells, 3):
    # 벽 설치: 원본 맵을 복사해 임시 격자에 반영
    temp_map = [row[:] for row in original_map]
    for r, c in wall_positions:
        temp_map[r][c] = 1

    safe_count = bfs_simulate(temp_map)
    max_safe = max(max_safe, safe_count)

print(max_safe)
