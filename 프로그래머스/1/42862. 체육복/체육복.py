def solution(n, lost, reserve):

    # 옷 가져왔는데 자기가 도난당한 경우 구해두고 시작
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)

    for i in sorted(real_reserve):
        # 앞 뒤 번호 학생 없는지 확인
        if i - 1 in real_lost:
            real_lost.remove(i-1)
        elif i + 1 in real_lost:
            real_lost.remove(i+1)

    return n-len(real_lost)
