import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

# 게이트 수
G = int(input())

# 비행기 수
P = int(input())

parent = [i for i in range(G+1)]

def find(x):

    # x의 루트 = 실제 도킹할 게이트 찾기
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

cnt = 0

for _ in range(P):
    g = int(input())

    # 도킹 가능한 게이트 찾기
    gate = find(g)

    # 도킹 가능한 게이트 없으면 폐쇄
    if gate == 0:
        break

    # 도킹 성공했으면 게이트랑 연결시키기
    parent[gate] = gate - 1
    cnt += 1

print(cnt)