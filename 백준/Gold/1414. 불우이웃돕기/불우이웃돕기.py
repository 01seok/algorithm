import sys
def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        if root_x < root_y:
            parents[root_y] = root_x
        else:
            parents[root_x] = root_y


def word_to_length(char):
    if 'a' <= char <= 'z':
        return ord(char) - ord('a') + 1
    elif 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 27
    return 0    # 0인 경우 연결 x

N = int(sys.stdin.readline())
edges = []
total_length = 0

for i in range(N):
    line = sys.stdin.readline()
    for j in range(N):
        length = word_to_length(line[j])
        if length > 0:
            total_length += length  # 랜선의 총 길이
            edges.append((length,i,j))  # cost, r, c
edges.sort()
parents = [i for i in range(N)]

total = 0
cnt = 0

for w, u, v in edges:
    if find_set(u) != find_set(v):
        union(u, v)
        total += w
        cnt += 1

        if cnt == N-1:
            break

if cnt < N-1:
    print(-1)
else:
    print(total_length - total)