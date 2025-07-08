def solution(video_len, pos, op_start, op_end, commands):

    def to_sec(t):
        m,s = map(int, t.split(':'))
        return m*60 + s

    def to_min(sec):
        m = sec // 60
        s = sec % 60
        return f'{m:02d}:{s:02d}'

    total_sec = to_sec(video_len)
    now_time = to_sec(pos)
    op_s = to_sec(op_start)
    op_e = to_sec(op_end)

    for cmd in commands:
        if op_s <= now_time <= op_e:
            now_time = op_e
        
        if cmd == 'prev':
            now_time = max(now_time-10, 0)
        else:
            now_time = min(now_time+10, total_sec)
        
        if op_s <= now_time <= op_e:
            now_time = op_e
    
    return to_min(now_time)