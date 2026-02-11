import sys
input = sys.stdin.readline

N, K, T = map(int, input().split())
shark_list = sorted(map(int, input().split()))

my_size = T
eat_list = []
idx = 0

for _ in range(K):
    while idx < N and shark_list[idx] < my_size:
        eat_list.append(shark_list[idx])
        idx += 1
    
    if not eat_list:
        break
    
    my_size += eat_list.pop()  # 가장 큰 것 (마지막에 들어온 것)

print(my_size)