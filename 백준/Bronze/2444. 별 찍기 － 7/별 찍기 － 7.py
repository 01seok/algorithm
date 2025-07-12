import sys

def solve():
    N = int(sys.stdin.readline()) # N 입력받기

    # 상단 피라미드 (1번째 줄부터 N번째 줄까지)
    for i in range(1, N + 1):
        # 공백 출력: N - i 개
        # 별 출력: 2 * i - 1 개
        print(' ' * (N - i) + '*' * (2 * i - 1))

    # 하단 역피라미드 (N+1번째 줄부터 2N-1번째 줄까지)
    # i는 1부터 N-1까지 반복
    for i in range(1, N):
        # 공백 출력: i 개
        # 별 출력: 2 * (N - i) - 1 개
        print(' ' * i + '*' * (2 * (N - i) - 1))

# 함수 호출
solve()