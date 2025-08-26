from collections import deque

N, K = map(int, input().split())


if N == K:
    print(0)
    print(1)
    exit()

q= deque()

MAX_POSITION = 100001

time = [-1] * MAX_POSITION
# 최소 시간 몇 개인지 구할 count 배열
count = [0] * MAX_POSITION

count[N] = 1
time[N] = 0

q.append(N)

while q:
    cur_pos = q.popleft()
    
    if cur_pos == K:
        continue

    next_pos_list = [cur_pos-1, cur_pos+1, cur_pos*2]
    for next_pos in next_pos_list:
        if 0 <= next_pos < MAX_POSITION:
            # 첫 방문
            if time[next_pos] == -1:
                time[next_pos] = time[cur_pos] + 1
                count[next_pos] = count[cur_pos]
                q.append(next_pos)
            
            # 첫 방문 아니지만, 최소 시간이 같다면
            elif time[next_pos] == time[cur_pos] + 1:
                count[next_pos] += count[cur_pos]

print(time[K])
print(count[K])