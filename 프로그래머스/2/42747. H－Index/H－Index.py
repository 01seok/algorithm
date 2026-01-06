def solution(citations):
    
    # 많이 인용된 것부터 확인하기
    # 인용 횟수 내림차순 정렬
    citations.sort(reverse=True)
    
    # 각 논문 확인하며 H-index 조건 검사
    for i in range(len(citations)):
        # 현재 논문 인용횟수 < 현재까지 논문 수면 h 가 더이상 커질 수 없음
        if citations[i] < i+1:
            return i
    
    # 반복문 끝날 때 까지 return 안됐으면 전체 논문 수가 정답
    return len(citations)