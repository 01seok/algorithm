import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))

path = []

def backtrack(start):
    if len(path) == M:
        print(*path)
        return

    for i in range(start, N):
        path.append(nums[i])
        backtrack(i)  # 같은 수 다시 선택 가능
        path.pop()

backtrack(0)