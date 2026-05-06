from itertools import product
from collections import deque

def solution(n, infection, edges, k):
    # 타입별 인접 리스트
    adj_by_type = [[[] for _ in range(n)] for _ in range(4)]

    for x, y, t in edges:
        x -= 1
        y -= 1
        adj_by_type[t][x].append(y)
        adj_by_type[t][y].append(x)
        
    #   i번 컴퓨터에서 감염 가능한 컴퓨터들의 비트마스크
    connected = [[0] * n for _ in range(4)]

    # 각 파이프 타입별로 연결 컴포넌트 계산
    for t in range(1, 4):
        visited = [False] * n

        for start in range(n):
            if visited[start]:
                continue

            q = deque([start])
            visited[start] = True

            nodes = []
            mask = 0

            # 같은 타입 파이프만 사용해서 연결된 컴퓨터들 BFS
            while q:
                cur = q.popleft()
                nodes.append(cur)

                # cur 컴퓨터를 비트마스크에 표시
                mask |= 1 << cur

                for nxt in adj_by_type[t][cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)

            # 같은 컴포넌트에 속한 모든 컴퓨터는
            # 해당 타입 파이프를 열면 서로 감염 가능
            for node in nodes:
                connected[t][node] = mask

    # 처음 감염된 컴퓨터
    infected_start = 1 << (infection - 1)

    answer = 1

    # k번 동안 열 파이프 타입 순서를 모두 시도
    # 예: k = 3이면 AAA, AAB, AAC, ABA ... CCC 전부 확인
    for order in product((1, 2, 3), repeat=k):
        infected = infected_start

        # 현재 순서대로 파이프를 하나씩 열어봄
        for t in order:
            next_infected = infected

            # 현재 감염된 컴퓨터들만 순회
            temp = infected
            while temp:
                # 가장 오른쪽에 있는 1비트 추출
                low_bit = temp & -temp

                # 해당 비트가 몇 번째 컴퓨터인지 계산
                node = low_bit.bit_length() - 1

                # node가 감염되어 있다면,
                # t 타입 파이프를 열었을 때 같은 컴포넌트 전체가 감염됨
                next_infected |= connected[t][node]

                # 방금 처리한 비트 제거
                temp -= low_bit

            infected = next_infected

        answer = max(answer, bin(infected).count("1"))

    return answer
