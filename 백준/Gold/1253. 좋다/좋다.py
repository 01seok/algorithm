import sys
input = sys.stdin.readline

N = int(input())
num_lst = list(map(int, input().split()))

num_lst.sort()
good = 0

for i in range(N):

    left = 0
    right = N - 1

    while left < right:

        if left == i:
            left += 1
            continue

        elif right == i:
            right -= 1
            continue

        if num_lst[left] + num_lst[right] == num_lst[i]:
            good += 1

            break

        elif num_lst[left] + num_lst[right] < num_lst[i]:
            left += 1

        else:
            right -= 1

print(good)