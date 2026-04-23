import sys
input = sys.stdin.readline

INF = float('inf')
T = int(input())
for _ in range(T):
    
    N, M = map(int, input().split())  # 방 개수 N, 통로 개수 M
    dist = [[INF] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):  # 자기 자신으로 가는 거리는 0
        dist[i][i] = 0  # i번 방에서 i번 방까지는 이동할 필요가 없으므로 0

    for _ in range(M):  # 통로 정보
        a, b, c = map(int, input().split())
        dist[a][b] = c  # 양방향 통로
        dist[b][a] = c

    for mid in range(1, N + 1):  # mid번 방을 거쳐 가는 경우를 확인
        for start in range(1, N + 1):  # 출발 방
            for end in range(1, N + 1):  # 도착 방
                if dist[start][end] > dist[start][mid] + dist[mid][end]:  # mid를 거쳐 가는 게 더 짧다면
                    dist[start][end] = dist[start][mid] + dist[mid][end]  # 최단거리 갱신

    K = int(input())  # 친구 수
    friends = list(map(int, input().split()))  # 친구들이 있는 방 번호

    answer_room = 1  # 정답 방 번호
    min_total_distance = INF  # 현재까지 찾은 최소 거리 합

    for room in range(1, N + 1):
        total_distance = 0  # 현재 room을 회의 장소로 했을 때 친구들의 거리 합

        for friend in friends:
            total_distance += dist[friend][room]

        if total_distance < min_total_distance:
            min_total_distance = total_distance
            answer_room = room

    print(answer_room)
