def solution(info, n, m):
    INF = 10**9

    # dp[b] = B도둑의 흔적이 b개일 때,
    # 가능한 A도둑의 최소 흔적 수
    dp = [INF] * m
    dp[0] = 0

    for a_trace, b_trace in info:
        next_dp = [INF] * m

        for b in range(m):
            # 아직 불가능한 상태는 건너뜀
            if dp[b] == INF:
                continue

            # 현재 물건을 A도둑이 훔치는 경우
            # A 흔적이 n 이상이면 잡히므로 n 미만이어야 함
            new_a = dp[b] + a_trace
            if new_a < n:
                next_dp[b] = min(next_dp[b], new_a)

            # 현재 물건을 B도둑이 훔치는 경우
            # B 흔적이 m 이상이면 잡히므로 m 미만이어야 함
            new_b = b + b_trace
            if new_b < m:
                next_dp[new_b] = min(next_dp[new_b], dp[b])

        dp = next_dp

    answer = min(dp)

    if answer == INF:
        return -1

    return answer