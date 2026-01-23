def solution(number, k):
    stack = []

    for num in number:
        # 스택 안에 숫자가 남아있고, 현재 숫자가 스택에 있는 숫자보다 크고 지울 k개가 남았다면
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1

        # 스택이 비었거나 위에서 더 작은 수 제거했다면 스택에 추가하고 다음 num 확인하기
        stack.append(num)

    # 이 작업들을 모두 끝냈는데
    # 더 지울 k개가 있을 수도 있음 (내림차순 정렬 되어있거나 같은 숫자 반복이면)
    # 그럼 뒤에서 k개 지워주기 (더 작은 숫자 일수록 뒤에있음)
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)