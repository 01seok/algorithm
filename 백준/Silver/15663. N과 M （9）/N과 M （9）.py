import sys
input = sys.stdin.readline

## 문제 요약
# N개의 자연수 중 M개를 고른 수열 출력 (배열에 중복된 수 있음, 같은 수열은 한 번만 출력)

## 알고리즘 유형
# 백트래킹 + 중복 수열 제거

## 핵심 아이디어
# 배열 정렬 후, 같은 재귀 깊이에서 이전과 같은 값이면 skip → 중복 수열 방지

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
seq = []
visited = [False] * N

def backtracking():

    if len(seq) == M:
        print(*seq)
        return

    prev = -1
    for i in range(N):
        if not visited[i]:

            if nums[i] == prev:
                continue
            prev = nums[i]
            seq.append(nums[i])
            visited[i] = True
            backtracking()
            seq.pop()
            visited[i] = False

backtracking()