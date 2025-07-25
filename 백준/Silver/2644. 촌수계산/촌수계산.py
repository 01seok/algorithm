import sys
input = sys.stdin.readline

N = int(input())    # 사람의 수
target_par, target_son = map(int, input().split())  # 두 사람의 관계의 촌수 = 정답
M = int(input())    # 관계의 수
adj_lst = [[] for _ in range(N+1)]  # 촌수 나타내는 인접 리스트
for _ in range(M):
    x, y = map(int, input().split())
    adj_lst[x].append(y)    # x는 y의 부모
    adj_lst[y].append(x)    # 부모 자식 관계는 양방향

visited = [-1] * (N+1)  # 1번 사람부터 N번 사람까지 촌수 계산 했는지 확인할 방문배열

def dfs(cur_node, distance):

    visited[cur_node] = distance

    for next_node in adj_lst[cur_node]:
        if visited[next_node] == -1:    # 아직 촌수 확인 안한 사람이라면
            dfs(next_node, distance+1)  # 촌수 1 증가시켜서 dfs


dfs(target_par, 0)
print(visited[target_son])