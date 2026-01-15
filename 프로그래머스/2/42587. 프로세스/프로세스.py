from collections import deque

def solution(priorities, location):
    q = deque()

    # (우선순위, idx) 만들어서 큐에 넣기
    for i in range(len(priorities)):
        priority = priorities[i]
        q.append((priority, i))
    
    # 인쇄 횟수
    answer = 0
    
    while q:
        # 맨 앞 꺼내기
        cur = q.popleft()
        cur_priority = cur[0]
        cur_idx = cur[1]
        
        # 남은 대기열 중 나보다 중요한 문서가 있는지 확인해보자
        # 큐에 남아있는 문서들의 우선순위랑 내 우선순위 비교 해보기
        higher_priority = False
        
        for doc in q:
            if doc[0] > cur_priority:
                higher_priority = True
                break
        
        # 더 중요한 문서가 있으면 다시 뒤로 넣기
        if higher_priority:
            q.append(cur)
        else:
            answer += 1
            
            # 인쇄한게 찾던 그 문서면 return
            if cur_idx == location:
                return answer
                
    return answer