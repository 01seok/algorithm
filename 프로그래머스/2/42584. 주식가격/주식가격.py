def solution(prices):
    n = len(prices)
    answer = [0] * n  # 결과 담을 배열

    # 현재 시점 잡기
    for i in range(n):
        # 다음 시점부터 끝까지 확인
        for j in range(i + 1, n):
            # 시간 1초 흘렀으므로 증가
            answer[i] += 1
            # 만약 가격이 내가 들어간 금액보다 떨어졌으면
            if prices[i] > prices[j]:
                break

    return answer
