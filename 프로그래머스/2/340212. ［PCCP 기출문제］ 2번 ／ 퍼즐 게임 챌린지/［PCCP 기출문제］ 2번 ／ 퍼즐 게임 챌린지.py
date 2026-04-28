def solution(diffs, times, limit):
    def can_solve(level):
        total = 0
        
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = times[i - 1] if i > 0 else 0
            
            if diff <= level:
                total += time_cur
            else:
                mistake = diff - level
                total += (time_cur + time_prev) * mistake + time_cur
            
            if total > limit:
                return False
        
        return True

    left = 1
    right = max(diffs)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        
        if can_solve(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer