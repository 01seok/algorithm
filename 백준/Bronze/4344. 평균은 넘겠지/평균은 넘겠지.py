import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    data = list(map(int, input().split()))
    n = data[0]
    scores = data[1:]
    avg = sum(scores) / n
    above = sum(1 for s in scores if s > avg)
    print(f"{above / n * 100:.3f}%")