# 완탐
# brown + yellow = 총 넓이
# 가로 >= 세로
# 1. 가로 x 세로 = 넓이 나오는 쌍 찾기
# 2. 가로 -2 x 세로 -2 = 노란색 개수

def solution(brown, yellow):
    total = brown + yellow

    # 세로는 3칸이 최소 되어야 노란색 타일 감쌀 수 있다.
    for h in range(3, total+1):
        
        # 약수면
        if total % h == 0:
            w = total // h
            
            if w >= h:
                if (w-2) * (h-2) == yellow:
                    return [w, h]