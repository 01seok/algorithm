n = int(input())

def is_hansu(x):
    s = list(map(int, str(x)))
    if len(s) <= 2:
        return True
    
    diff = s[1] - s[0]
    for i in range(1, len(s) - 1):
        if s[i+1] - s[i] != diff:
            return False
    return True

count = 0
for i in range(1, n + 1):
    if is_hansu(i):
        count += 1

print(count)