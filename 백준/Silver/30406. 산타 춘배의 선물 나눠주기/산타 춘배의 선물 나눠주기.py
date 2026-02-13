import sys
input = sys.stdin.readline

N = int(input())
cnt = [0] * 4
for p in map(int, input().split()):
    cnt[p] += 1

ans = 0

# (0,3) 매칭 XOR=3
pair = min(cnt[0], cnt[3])
ans += pair * 3
cnt[0] -= pair
cnt[3] -= pair

# (1,2) 매칭 XOR=3
pair = min(cnt[1], cnt[2])
ans += pair * 3
cnt[1] -= pair
cnt[2] -= pair

# (0,2) 매칭 XOR=2
pair = min(cnt[0], cnt[2])
ans += pair * 2
cnt[0] -= pair
cnt[2] -= pair

# (1,3) 매칭 XOR=2
pair = min(cnt[1], cnt[3])
ans += pair * 2
cnt[1] -= pair
cnt[3] -= pair

# (0,1) 매칭 XOR=1
pair = min(cnt[0], cnt[1])
ans += pair * 1

# (2,3) 매칭 XOR=1
pair = min(cnt[2], cnt[3])
ans += pair * 1

print(ans)