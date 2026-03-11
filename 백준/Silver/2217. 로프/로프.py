import sys

n = int(sys.stdin.readline())
ropes = [int(sys.stdin.readline()) for _ in range(n)]

ropes.sort()

max_weight = 0

for i in range(n):
    weight = ropes[i] * (n - i)
    max_weight = max(max_weight, weight)

print(max_weight)