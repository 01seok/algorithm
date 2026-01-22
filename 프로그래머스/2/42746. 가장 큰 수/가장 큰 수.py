def solution(numbers):
    # 문자열로 변환
    numbers = list(map(str, numbers))

    # 각 문자열을 3번 반복한 값으로 정렬 (내림차순)
    numbers.sort(key=lambda x: x * 3, reverse=True)

    # 이어 붙이기
    answer = ''.join(numbers)

    # 예외 처리
    if answer[0] == '0':
        return '0'
        
    else:
        return answer
    