def solution(N, results):

    # 경기 결과 담을 2차원 리스트
    result_lst = [[0] * (N+1) for _ in range(N+1)]

    # 경기 결과 기록
    for winner, loser in results:
        result_lst[winner][loser] = 1
        result_lst[loser][winner] = -1

    # 경기 결과 모르는 선수 추론하기
    for dont_know in range(1, N+1):
        for first in range(1, N+1):
            for second in range(1, N+1):
                # first 선수가 결과 모르는 선수 이기고, 모르는 선수가 second 이기면
                # first 선수는 second 이긴 것
                # i가 k를 이기고, k가 j를 이겼다면 -> i는 j를 이긴 것이다.
                if result_lst[first][dont_know] == 1 and result_lst[dont_know][second] == 1:
                    result_lst[first][second] = 1
                    result_lst[second][first] = -1
    answer = 0
    for i in range(1, N+1):
        cnt = 0
        for j in range(1, N+1):
            # 자기 자신이 아니면서 승패 관계가 확실한 경우 카운트
            if result_lst[i][j] != 0:
                cnt += 1
        # 자신을 제외한 모든 선수와의 경기 결과 알 수 있으면 정확한 순위 매길 수 있음
        if cnt == N-1:
            answer += 1

    return answer