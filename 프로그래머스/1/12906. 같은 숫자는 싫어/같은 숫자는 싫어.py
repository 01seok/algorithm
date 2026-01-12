def solution(arr):
    answer = []
    
    for num in arr:
        # 비어있으면 넣기
        # num이 answer의 마지막 숫자와 다르면 넣기
        if len(answer) == 0 or answer[-1] != num:
            answer.append(num)
        
            
    return answer