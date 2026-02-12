N, M = map(int, input().split())
meats = []

for _ in range(N):
    weight, cost = map(int, input().split())
    # 가격 오름차순, 무게 내림차순
    meats.append((cost, -weight))

meats.sort()

ans = float('inf')
total_w = 0
total_c = 0
pre_cost = -1

for next_cost, next_weight in meats:
    weight = -next_weight

    # 가격 같으면 비용 추가
    if next_cost == pre_cost:
        total_c += next_cost

    # 더 비싸면 그 가격으로 갱신
    else:
        total_c = next_cost

    total_w += weight
    pre_cost = next_cost

    if total_w >= M:
        ans = min(ans, total_c)

if ans == float('inf'):
    print(-1)
else:
    print(ans)