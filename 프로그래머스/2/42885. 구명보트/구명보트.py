def solution(people, limit):

    # 구명보트 - 지난 A형 모자 문제와 유사한 듯함
    # 투 포인트로 가장 무거운 사람과 가장 가벼운 사람을 매치하여 태워보기

    # 오름차순 정렬
    people.sort()

    # 투포인터 초기화
    light_idx = 0
    heavy_idx = len(people) - 1

    boat_cnt = 0

    # 두 포인터 교차 시점까지 반복 (1명이 남아도 처리해야함)
    while light_idx <= heavy_idx:

        # 가장 무거운 사람과 가장 가벼운 사람 무게 합이 제한 무게 이하면 같이 탈 수 있음
        if people[light_idx] + people[heavy_idx] <= limit:
            # 가벼운 사람 한 명 보내고
            light_idx += 1

        # 무거운 사람은 무조건 타고 가니까
        heavy_idx -= 1
        boat_cnt += 1

    return boat_cnt