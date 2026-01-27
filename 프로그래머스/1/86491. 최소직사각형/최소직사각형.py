def solution(sizes):
    
    # 가로 세로 나눌거 없이 회전 되니까 가장 긴거 중 긴거, 가장 짧은 길이 중 최대 길이
    max_w = max(max(w,h) for w, h in sizes)
    max_h = max(min(w,h) for w, h in sizes)
    
    return max_w * max_h
