from collections import deque
def solution(bridge_length, weight, truck_weights):

    # 대기 트럭 무게들 큐로 변환해서 popleft 사용
    trucks = deque(truck_weights)

    # 다리 건너는 트럭 (실제 다리 위 공간임)
    bridge = deque([0] * bridge_length)

    time = 0
    cur_weight = 0

    while trucks:
        time += 1
        
        # 지금 트럭 나가면 현재 다리 하중 중량에서 빼주기
        cur_truck = bridge.popleft()
        cur_weight -= cur_truck
        
        if cur_weight + trucks[0] <= weight:
            # 지금 다리 하중 무게 + 담 트럭 무게 되면 출발
            truck = trucks.popleft()
            bridge.append(truck)
            cur_weight += truck
            
        else:
            # 못가면 다음 트럭 도착할 때 까지 0 넣어서 시간 흐르게
            bridge.append(0)
    
    # 마지막 트럭 걸리는 시간까지 더해주기
    time += bridge_length
    
    return time