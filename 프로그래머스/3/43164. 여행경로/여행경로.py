
'''
ticket은 [출발지, 도착지], 항상 인천에서 출발
모든 항공권 사용, 경로 여러 개 가능하면 알파벳 앞서는 경로
'''

def solution(tickets):

    # 알파벳 순으로 정렬
    tickets.sort()

    # 여행 경로 담을 리스트
    route = []

    visited = [False] * len(tickets)

    def dfs(cur, path):

        # 모든 티켓 다 쓰면 종료
        if len(path) == len(tickets) + 1:
            # 경로 복사해서
            route.append(path[:])
            return True

        for i in range(len(tickets)):

            if not visited[i] and tickets[i][0] == cur:
                visited[i] = True
                
                # 지금 위치에서 여행 마칠 수 있는지 확인
                if dfs(tickets[i][1], path+ [tickets[i][1]]):
                    return True
                
                # 다음 경로 확인 위해서 방문 기록 지우기
                visited[i] = False
        
        return False
    
    dfs("ICN", ["ICN"])
    
    return route[0]
                