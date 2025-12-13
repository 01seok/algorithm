import sys

input = sys.stdin.readline

# 가로, 세로, 인벤에 있는 초기 블록 개수
N, M, B = map(int, input().split())

field = []
for _ in range(N):
    field.append(list(map(int, input().split())))

total_time = float('inf')
total_height = 0

# 땅의 높이는 0 ~ 256까지 가능하니 모든 높이 다 맞춰보기
for h in range(257):

    # 높이를 맞추기 위해 제거할 블록이랑 사용할 블록 개수
    remove_block = 0
    use_block = 0

    for r in range(N):
        for c in range(M):
            cur_height = field[r][c]

            # 현재 땅이 목표 높이보다 높으면 제거
            if cur_height > h:
                remove_block += (cur_height - h)

            # 현재 땅이 목표보다 낮으면 채우기
            else:
                use_block += (h - cur_height)

    # 블록 갯수 검증
    if use_block > remove_block + B:
        continue

    time = remove_block * 2 + use_block

    # 최소 시간 갱신
    if time <= total_time:
        total_time = time
        total_height = h

print(total_time, total_height)
