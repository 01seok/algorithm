T = int(input())
for tc in range(T):
    N = int(input())
    # dp 테이블 생성 (n은 1~11)
    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, 11):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[N])