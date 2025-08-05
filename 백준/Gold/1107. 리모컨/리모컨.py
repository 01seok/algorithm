N = int(input())
M = int(input())

if M:
    broken = set(input().split())
else:
    broken = set()

min_click = abs(N-100)  # 현재 100번

for channel in range(1000000):
    for digit in str(channel):
        if digit in broken:
            break

    else:
        click = len(str(channel)) + abs(channel - N)
        min_click = min(min_click, click)
print(min_click)