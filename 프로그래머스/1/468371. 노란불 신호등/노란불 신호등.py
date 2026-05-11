from math import gcd

def solution(signals):
    # 두 수의 최소공배수
    def lcm(a, b):
        return a * b // gcd(a, b)

    # 전체 신호 상태가 반복되는 주기
    limit = 1
    for G, Y, R in signals:
        cycle = G + Y + R
        limit = lcm(limit, cycle)

    # 시간은 1초부터 시작
    for time in range(1, limit + 1):
        all_yellow = True

        for G, Y, R in signals:
            cycle = G + Y + R

            # time = 1일 때 초록불의 첫 번째 초이므로 time - 1 기준으로 계산
            current = (time - 1) % cycle

            if not (G <= current < G + Y):
                all_yellow = False
                break

        if all_yellow:
            return time

    return -1