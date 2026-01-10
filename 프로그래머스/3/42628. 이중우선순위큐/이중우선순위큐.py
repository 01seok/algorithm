import heapq

# 최소 힙, 최대 힙 두 개 동시에 운용하기
# 최대 힙에 넣을 땐 음수 부호 달아서 넣고, 뺄 때는 다시 양수로 빼주기
# 최소 힙 최대 힙 동시에 두 개 쓰니까 remove 제때 제때 잘해주기
def solution(operations):

    min_heap = []
    max_heap = []

    for o in operations:
        command, num = o.split()
        num = int(num)

        if command == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)

        elif command == "D":

            if not min_heap:
                continue

            # 최대값 삭제
            if num == 1:
                max_val = -heapq.heappop(max_heap)
                min_heap.remove(max_val)

            else:
                # 최소값 삭제
                min_val = heapq.heappop(min_heap)
                max_heap.remove(-min_val)

    if not min_heap:
        return [0,0]

    return [-max_heap[0], min_heap[0]]