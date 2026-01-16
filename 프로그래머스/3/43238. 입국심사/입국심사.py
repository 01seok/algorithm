def solution(n, times):
    # 최소힙으로 풀고싶었는데 .. n이 10억이네 ..
    # 무조건 이분 탐색

    answer = 0

    # 좌, 우 범위 범위 설정
    left = 1
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2

        # mid분 동안 몇 명 가능한지 계산하자
        # 몇 명 심사했는지 확인할 변수
        people = 0

        for t in times:
            people += mid // t

            # 이미 검사 인원 넘었으면 할 필요 xxx
            if people >= n:
                break

        # 목표 인원 채운거보고 여유 있는지 더 빡빡하게 돌려야할지 결정
        if people >= n:
            answer = mid    # 이게 답일수도 있으니 저장해두고
            right = mid - 1 # 여유있으니 줄여보기
        else:
            left = mid + 1

    return answer