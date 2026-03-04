h, m, s = map(int, input().split())
t = int(input())

total = h * 3600 + m * 60 + s + t
total %= 24 * 3600

h = total // 3600
total %= 3600
m = total // 60
s = total % 60

print(h, m, s)