def solution(routes):

    # 진출 시점 기준으로 오름차순 정렬
    routes.sort(key=lambda x : x[1])

    cnt = 0
    # 마지막으로 설치된 카메라 위치 초기화
    last_camera = -30001
    
    for start, end in routes:
        # 이번 차가 카메라 설치 후에 들어왔으면 카메라 설치해줘야함 (이 차 나갈 때 설치)
        if start > last_camera:
            cnt += 1
            last_camera = end
            
    return cnt
