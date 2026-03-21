import sys
input = sys.stdin.readline

## 문제 요약
# N개의 자연수 중 M개를 고른 수열 출력 (중복 없이, 사전 순 정렬)

## 알고리즘 유형
# 백트래킹 / 순열

## 핵심 아이디어
# 15649(N과M 1)과 동일한 구조, 단 입력이 배열 → 정렬 후 동일한 백트래킹 적용
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * N
seq = []
def backtracking():

    if len(seq) == M:
        print(*seq)
        return

    prev = -1
    for i in range(N):
        if not visited[i]:

            if prev == nums[i]:
                continue

            prev = nums[i]
            seq.append(nums[i])
            visited[i] = True
            backtracking()
            seq.pop()
            visited[i] = False

backtracking()