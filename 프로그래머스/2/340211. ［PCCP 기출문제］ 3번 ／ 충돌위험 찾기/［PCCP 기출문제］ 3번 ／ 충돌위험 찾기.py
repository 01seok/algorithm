from collections import defaultdict

def solution(points, routes):
    answer = 0
    time_pos = defaultdict(lambda: defaultdict(int))

    for route in routes:
        # 시작 포인트
        r, c = points[route[0] - 1]
        time = 0
        time_pos[time][(r, c)] += 1

        # 다음 포인트들로 이동
        for i in range(1, len(route)):
            nr, nc = points[route[i] - 1]

            # r 좌표 먼저 이동
            while r != nr:
                if r < nr:
                    r += 1
                else:
                    r -= 1

                time += 1
                time_pos[time][(r, c)] += 1

            # c 좌표 이동
            while c != nc:
                if c < nc:
                    c += 1
                else:
                    c -= 1

                time += 1
                time_pos[time][(r, c)] += 1

    # 같은 시간에 같은 좌표에 2대 이상 있으면 충돌 위험 1회
    for positions in time_pos.values():
        for count in positions.values():
            if count >= 2:
                answer += 1

    return answer