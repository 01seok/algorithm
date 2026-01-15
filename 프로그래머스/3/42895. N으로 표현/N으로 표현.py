'''
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.
'''

# 5를 1번 쓴 숫자들 + 사칙연산 + 5를 2번 쓴 숫자들
# 5를 2번 쓴 숫자들 + 사칙연산 + 5를 1번 쓴 숫자들

# N을 K번 사용해서 만들 수 있는 수
# k번 사용 집합 = {N을 K번 이어 붙인 수} + {(i번 집합) 사칙연산 (K-i번 집합)}

def solution(N, number):

    # N = number
    if N == number:
        return 1

    # N을 i번 써서 만들 수 있는 숫자들 모임
    # dp table 세팅 (1 ~ 8까지 세팅)
    dp = [set() for _ in range(8)]
    for k in range(1, 9):

        # 단순하게 이어 붙인 숫자 넣기
        # i번 사용했으니 dp[i-1]에 저장해두기
        dp[k-1].add(int(str(N) * k))

        for i in range(1, k):
            j = k - i # 나머지 횟수

            # dp 테이블 idx -1, 조합 가능한 숫자 다 넣기
            for case1 in dp[i-1]:
                for case2 in dp[j-1]:
                    dp[k-1].add(case1 + case2)
                    dp[k-1].add(case1 - case2)
                    dp[k-1].add(case1 * case2)
                    if case2 != 0:
                        dp[k-1].add(case1 // case2)

        # 이번 바구니에 목표 숫자 있는지 체크
        if number in dp[k-1]:
            return k

    # 8번 바구니까지 다 돌았는데 없으면 -1
    return -1


