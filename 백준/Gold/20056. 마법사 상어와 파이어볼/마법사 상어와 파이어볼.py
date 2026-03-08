import sys
from collections import defaultdict

input = sys.stdin.readline

# 방향은 문제에서 제시했음
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

# 격자 크기, 초기 파이어볼 개수, 명령 횟수
N, M, K = map(int, input().split())

fireballs = []  # 현재 턴의 파이어볼들 저장할 리스트
for _ in range(M):
    r,c,m,s,d = map(int, input().split())   # 위치, 질량, 속력, 방향
    fireballs.append((r-1, c-1, m, s, d))   # index 1부터 시작이니 -1

# 명령 K번
for _ in range(K):
    # 이동 후 도착한 칸에 있는 파이어볼들 모아둘 곳
    temp_cell = defaultdict(list)

    for r,c,m,s,d in fireballs:
        nr, nc = (r + dr[d] * s) % N, (c + dc[d] * s) % N # 범위 벗어나면 다시 반대 앞으로 돌아와야함
        temp_cell[(nr,nc)].append((m,s,d))  # 도착한 칸에 리스트로 쌓아두기

    # 다음 턴에 쓸 파이어볼 정보 리스트
    next_fireballs = []

    for (r, c), items in temp_cell.items(): # 도착한 칸에 모여있는 파이어볼들 처리
        if len(items) == 1: # 1개 밖에 없으면
            m,s,d = items[0]
            next_fireballs.append((r,c,m,s,d))
            continue

        total_m = 0
        total_s = 0
        zzak_cnt = 0    # 방향 짝수 파이어볼 수
        hol_cnt = 0     # 방향 홀수 파이어볼 수
        cnt = len(items)# 모여있는 파이어볼 수

        for m, s, d in items:
            total_m += m
            total_s += s

            # 방향 짝수면
            if d % 2 == 0:
                zzak_cnt += 1
            else:
                hol_cnt += 1

        new_m = total_m // 5
        if new_m == 0:
            continue

        new_s = total_s // cnt

        if zzak_cnt == cnt or hol_cnt == cnt:
            new_d = [0,2,4,6]
        else:
            new_d = [1,3,5,7]

        for nd in new_d:
            next_fireballs.append((r,c,new_m, new_s, nd))

    fireballs = next_fireballs
    
ans = 0
for r,c,m,s,d in fireballs:
    ans += m
print(ans)