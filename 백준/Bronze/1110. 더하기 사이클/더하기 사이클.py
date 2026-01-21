n = int(input().strip())
start = n
cnt = 0

while True:
    a = n // 10
    b = n % 10
    n = b * 10 + (a + b) % 10
    cnt += 1
    if n == start:
        break

print(cnt)