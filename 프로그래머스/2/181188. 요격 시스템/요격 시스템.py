def solution(targets):
    # 끝나는 지점 e를 기준으로 오름차순 정렬
    targets.sort(key=lambda x: x[1])

    answer = 0

    # 마지막으로 요격 미사일을 쏜 위치
    # 처음에는 아무 미사일도 쏘지 않았으므로 -1로 둠
    intercept = -1

    for s, e in targets:
        # 현재 미사일의 시작점 s가 기존 요격 위치 이상이면
        # 기존 요격 미사일로는 이 미사일을 요격할 수 없음
        if intercept <= s:
            answer += 1

            intercept = e

    return answer