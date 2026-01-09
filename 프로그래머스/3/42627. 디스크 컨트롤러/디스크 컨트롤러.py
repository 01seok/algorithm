# 힙을 이용하기
# 우선 순위 : 작업 소요시간 짧은 것, 작업 요청 시작 시간 빠른 것, 작업 번호 작은 것 순서
# 이미 작업하고 있는데 다른 작업 들어오면 큐에 저장한 뒤 하던 작업 끝내고
# 우선순위 확인 후 다음 순서 작업 시작
# 현재 작업 안하고 있는데 아직 남은 작업이 있는 경우에는 다음 작업 요청 시간으로 이동 시켜주기

import heapq

def solution(jobs):

    # 작업 번호 정렬 = 작업 요청 시간 빠른 순 정렬
    jobs.sort()

    # 작업 수 : cnt, 현재 시간 : now_time, 총 소요시간 total_time
    cnt = 0
    now_time = 0
    total_time = 0

    # 우선순위 큐 (작업 소요 시간을 기준으로 최소 힙)
    q = []

    # 작업 번호
    i = 0
    while cnt < len(jobs):

        # 현재 시간 이전에 들어온 요청 모두 힙에 넣기
        while i < len(jobs) and jobs[i][0] <= now_time:
            # (소요시간, 요청 시간)
            heapq.heappush(q, (jobs[i][1], jobs[i][0]))
            i += 1

        # 현재 작업 대기 중인 일이 있으면
        if q:
            require_time, request_time = heapq.heappop(q)
            now_time += require_time # 작업 끝난 시간으로 갱신
            total_time += (now_time - request_time) # 작업 요청 후 작업 끝날 때 까지의 시간이 총 소요시간이므로
            cnt += 1

        # 아직 작업은 안 들어왔지만 들어올 일이 있으면 그 시간으로 이동
        else:
            now_time = jobs[i][0]

    return total_time // len(jobs)
