import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

path = []

def backtrack():
    if len(path) == M:
        print(*path)
        return

    prev = -1
    for i in range(N):
        if nums[i] == prev:
            continue

        prev = nums[i]
        path.append(nums[i])
        backtrack()
        path.pop()

backtrack()