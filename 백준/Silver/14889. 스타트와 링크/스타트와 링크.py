import sys

input = sys.stdin.readline

N = int(input())

stat_lst = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N

ans = float('inf')

def dfs(player_num, cnt):
    global ans
    
    # 전체 인원 절반만큼 모이면 능력치 계산
    if cnt == N // 2:
        start_sum = 0
        link_sum = 0
        
        # 전체 인원 순회하며 팀 능력치 계산
        for i in range(N):
            for j in range(N):
                
                # 둘이 같은 스타트 팀이면
                if visited[i] and visited[j]:
                    start_sum += stat_lst[i][j]
                
                elif not visited[i] and not visited[j]:
                    link_sum += stat_lst[i][j]
        ans = min(ans, abs(start_sum - link_sum))
        
    # 중복 없는 조합 만들기
    for i in range(player_num, N):
        if not visited[i]:
            visited[i] = True
            # 재귀로 다음 멤버 뽑기 (전체 절반 인원 될 때 까지)
            dfs(i+1, cnt+1)
            # 다른 경우 체크하기 위해 원상복구
            visited[i] = False

dfs(0, 0)
print(ans)