n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
s, e = 0, 0
total = 0
while True:
    if total >= m:
        if total == m:
            cnt += 1
        total -= arr[s]
        s += 1
    elif e == n:
        break
    else:
        total += arr[e]
        e += 1
print(cnt)