import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

count = 0

for i in a:
    count += 1
    i -= b
    if i > 0:
        count += (i + c - 1) // c

print(count)