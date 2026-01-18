# 오른쪽이나 아래로만 갈 수 있음
# 현재 칸 경로 수 = 위쪽 칸 경로 수 + 왼쪽칸 경로 수

# m = 가로, n = 세로
def solution(m, n, puddles):

    dp = [[0] * (m+1) for _ in range(n+1)]

    # 집은 경우의 수 1
    dp[1][1] = 1

    for r in range(1, n+1):
        for c in range(1, m+1):

            if r == 1 and c == 1:
                continue

            # 웅덩이 못가니 경웅의 수 0으로
            if [c,r] in puddles:
                dp[r][c] = 0

            else:
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

    return dp[n][m] % 1000000007