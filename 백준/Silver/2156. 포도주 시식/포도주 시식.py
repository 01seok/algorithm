# 완탐하면 무조건 시초..
#연속 세잔 마실 수 없으니 연속된 세잔 중 최대가 되는 2잔 합을 dp 배열에 저장하면서 끝까지 봐야함
N = int(input())
wine = [int(input()) for _ in range(N)]

if N == 1:
    print(wine[0])

elif N == 2:
    print(wine[0] + wine[1])

else:

    dp = [0] * N

    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[1], wine[0] + wine[2], wine[1] + wine[2])

    for i in range(3, N):
        dp[i] = max(
            # i번 와인 안 마신 경우
            dp[i-1],
            # i-1번 와인 안 마신 경우
            dp[i-2] + wine[i],
            # i-2 안 마시고 i, i-1 마신 경우
            dp[i-3] + wine[i-1] + wine[i]
        )

    print(dp[N-1])