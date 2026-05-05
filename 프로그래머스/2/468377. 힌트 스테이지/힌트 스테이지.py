def solution(cost, hint):
    n = len(cost)
    answer = float("inf")

    # 각 번들을 샀을 때 얻는 힌트권 개수 전처리
    bundle_price = []
    bundle_tickets = []

    for h in hint:
        price = h[0]
        tickets = [0] * n

        for stage_num in h[1:]:
            tickets[stage_num - 1] += 1

        bundle_price.append(price)
        bundle_tickets.append(tickets)

    # hint는 n-1개
    for mask in range(1 << (n - 1)):
        total = 0
        tickets = [0] * n

        # 어떤 번들을 살지 결정
        for i in range(n - 1):
            if mask & (1 << i):
                total += bundle_price[i]

                for j in range(n):
                    tickets[j] += bundle_tickets[i][j]

        # 각 스테이지 해결 비용 계산
        for i in range(n):
            use_count = min(tickets[i], n - 1)
            total += cost[i][use_count]

            if total >= answer:
                break

        answer = min(answer, total)

    return answer