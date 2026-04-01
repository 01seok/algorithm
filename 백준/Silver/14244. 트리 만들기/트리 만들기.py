n, m = map(int, input().split())

# 0 ~ (n-m)까지 일자로 연결
for i in range(n - m):
    print(i, i + 1)

# 남은 정점들을 (n-m)에 연결
for i in range(n - m + 1, n):
    print(n - m, i)