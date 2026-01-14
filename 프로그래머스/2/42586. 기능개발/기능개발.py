import math

def solution(progresses, sppeds):
    answer = []

    # 각 작업 며칠 걸리는지 담아둘 리스트
    days = []

    # 각 기능이 며칠 걸리는지 계산해두기
    for i in range(len(progresses)):
        progress_now = progresses[i]
        speed_now = sppeds[i]

        remain_day = math.ceil((100 - progress_now) / speed_now)
        days.append(remain_day)

    # 첫번째 배포 날
    release_day = days[0]

    # 이번 배포에 포함될 작업 수
    cnt = 0

    for day in days:
        if day <= release_day:
            cnt += 1

        # 배포 날짜보다 오래 걸리면 앞에 쌓여있는 작업들 배포하기 다시 시작
        else:
            answer.append(cnt)

            # 배포됐으니 다시 작업 수 1로 초기화
            cnt = 1
            # 다음 배포날짜 갱신
            release_day = day

    # 마지막에 세고있던 그룹도 넣어주기
    answer.append(cnt)

    return answer