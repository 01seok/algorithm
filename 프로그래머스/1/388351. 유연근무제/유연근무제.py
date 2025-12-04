# 시간을 분 단위로 변환하는 헬퍼 함수
def to_minutes(time):
    # 100으로 나눈 몫이 시간(h)
    h = time // 100
    # 100으로 나눈 나머지가 분(m)
    m = time % 100
    # 전체를 분으로 환산하여 반환
    return h * 60 + m

def solution(schedules, timelogs, startday):
    answer = 0
    
    # 전체 직원 수(리스트의 길이)
    n = len(schedules)
    
    # 0번 직원부터 n-1번 직원까지 인덱스로 접근하여 반복
    for i in range(n):
        
        # i번째 직원의 희망 출근 시간 가져오기
        target_time = schedules[i]
        
        # i번째 직원의 일주일 출근 기록 리스트 가져오기
        my_logs = timelogs[i]
        
        # 인정되는 마지노선 시간 계산 (희망 시간 + 10분)
        deadline = to_minutes(target_time) + 10
        
        # 지각 없이 성공했는지 체크하는 플래그 변수
        is_success = True
        
        # 일주일(7일) 동안의 기록 확인
        for j in range(7):
            # 오늘의 요일 계산 (1 = 월, 7=일)
            current_day_mod = (startday + j) % 7
            
            # 토요일(나머지 6)이나 일요일(나머지 0)이면 체크 건너뜀
            if current_day_mod == 6 or current_day_mod == 0:
                continue
            
            # 해당 요일(j번째 날)의 실제 출근 시간을 분으로 변환
            arrival_time = to_minutes(my_logs[j])
            
            # 마지노선보다 늦게 왔다면 (초과했다면)
            if arrival_time > deadline:
                is_success = False
                # 한 번이라도 지각하면 실패이므로 더 볼 필요 없음
                break
        
        # for문이 끝난 후에도 성공 플래그면 상품 받을 사람 수 증가
        if is_success:
            answer += 1
            
    return answer