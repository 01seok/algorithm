import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(set(map(int, input().split())))

path = []

def backtrack(start):
    if len(path) == M:
        print(*path)
        return

    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(i)
        path.pop()

backtrack(0)