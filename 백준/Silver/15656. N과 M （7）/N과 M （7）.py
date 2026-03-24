import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

path = []

def backtrack():
    if len(path) == M:
        print(*path)
        return

    for i in range(N):
        path.append(nums[i])
        backtrack()
        path.pop()

backtrack()