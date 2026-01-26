def solution(numbers, target):
    answer = 0

    def dfs(idx, cur_sum):
        nonlocal answer
        
        # 숫자 다썼는데 목표 숫자면
        if idx == len(numbers):
            if cur_sum == target:
                answer += 1

            return
        
        # 다음 idx 확인, +, - 둘 다 돌리기
        dfs(idx +1, cur_sum + numbers[idx])
        dfs(idx+1, cur_sum - numbers[idx])

    dfs(0, 0)
    return answer
