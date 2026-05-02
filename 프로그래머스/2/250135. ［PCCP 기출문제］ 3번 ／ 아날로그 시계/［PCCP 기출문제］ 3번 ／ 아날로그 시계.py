def solution(h1, m1, s1, h2, m2, s2):
    def to_second(h, m, s):
        return h * 3600 + m * 60 + s

    def count_until(t):
        # 00:00:00 이후부터 t초까지, 즉 (0, t] 범위의 알람 횟수

        # 초침-분침 겹침 횟수
        minute_count = (t * 59) // 3600

        # 초침-시침 겹침 횟수
        hour_count = (t * 719) // 43200

        count = minute_count + hour_count

        # 12:00:00에는 초침, 분침, 시침이 모두 겹치지만 알람은 1번만 울림
        if t >= 43200:
            count -= 1

        return count

    start = to_second(h1, m1, s1)
    end = to_second(h2, m2, s2)

    answer = count_until(end) - count_until(start)

    # 시작 시각도 포함해야 하므로,
    # 시작 시각에 이미 초침이 분침 또는 시침과 겹쳐 있으면 1회 추가
    if (start * 59) % 3600 == 0 or (start * 719) % 43200 == 0:
        answer += 1

    return answer