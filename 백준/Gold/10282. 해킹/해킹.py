import sys
import heapq

testcase = int(input())

for tc in range(testcase):
    n, d, c = map(int, input().split())
    adj_lst = [[] for _ in range(n+1)]  # 컴퓨터 번호는 1번 부터
    INF = float('inf')
    dist = [INF] * (n+1)
    for _ in range(d):
        a,b,s = map(int, input().split())
        adj_lst[b].append((s, a))   # a가 b에 의존한다 = b가 감염되면 s초 뒤에 a도 감염된다이므로

    pq = []
    dist[c] = 0 # 처음 해킹 당한 컴퓨터 c, 걸린시간 0초
    heapq.heappush(pq, (0, c))

    while pq:
        cost, cur_node = heapq.heappop(pq)

        if cost > dist[cur_node]:
            continue

        for next_cost, next_node in adj_lst[cur_node]:
            new_cost = cost + next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    infected_cnt = 0
    last_computer_time = 0

    for i in range(1, n+1):
        if dist[i] != INF:
            infected_cnt += 1
            if dist[i] > last_computer_time:
                last_computer_time = dist[i]
    print(infected_cnt, last_computer_time)