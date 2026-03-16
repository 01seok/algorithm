nums = set(range(1, 10001))
generated = set()

for i in range(1, 10001):
    n = i
    total = i
    while n > 0:
        total += n % 10
        n //= 10
    generated.add(total)

for num in sorted(nums - generated):
    print(num)