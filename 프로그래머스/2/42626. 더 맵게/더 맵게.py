import heapq

def solution(scoville, K):

    # 모든 요소를 힙으로 만들어야함
    heapq.heapify(scoville)

    # 섞은 횟수
    cnt = 0

    # 제일 안 매운 음식이 목표치보다 매워지면 끝
    while scoville[0] < K:

        # 할 수 없는 경우
        if len(scoville) < 2:
            return -1

        # 제일 안 매운 두개 순서대로 꺼내기
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        # 섞어서 다시 넣기
        new = first + (second * 2)
        heapq.heappush(scoville, new)

        cnt += 1

    return cnt