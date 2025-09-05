import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    x, y = a, b
    while y:
        x, y = y, x % y
    print(a * b // x)