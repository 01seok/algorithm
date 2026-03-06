import sys

input = sys.stdin.readline

N, M, L = map(int, input().split())
num_of_cut = []
can_cut_lst = []

for _ in range(M):
    can_cut_lst.append(int(input()))

can_cut_lst.sort()

for _ in range(N):
    num_of_cut.append(int(input()))

def can_cut(can_cut_lst, L, Q, mid):
    prev = 0   # 마지막으로 자른 위치 (처음엔 케이크 시작점)
    cuts = 0   # 자른 횟수

    for pos in can_cut_lst:
        if pos - prev >= mid:  # 이전 커팅 위치로부터 mid 이상 떨어져 있으면
            prev = pos         # 여기서 자른다
            cuts += 1          # 자른 횟수 증가
            if cuts == Q:   # Q번 다 잘랐으면 끝
                break

    # Q번 못 잘랐으면 실패
    if cuts < Q:
        return False

    return L - prev >= mid


for Q in num_of_cut:        # N개 각각 처리
    left = 0
    right = L

    while left <= right:
        mid = (left + right) // 2   # 이번에 시도할 최소 조각 길이

        if can_cut(can_cut_lst, L, Q, mid): # mid로 Q번 자를 수 있으니 더 큰 값 시도
            left = mid + 1
        else:
            right = mid - 1 # 더 작은 값 시도


    print(right)