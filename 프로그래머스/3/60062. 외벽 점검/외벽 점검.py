from itertools import permutations

def solution(N, weak, dist):

    # 원형을 선형으로 변환
    weak = weak + [w + N for w in weak]

    # 친구 한 명씩 늘리면서 순열
    for cnt in range(1, len(dist) + 1):
        for perm in permutations(dist, cnt):
            for start in range(len(weak)//2):
                idx = start # 현재 확인할 취약점 인덱스
                for friend in perm:
                    # 지금 친구가 weak[idx] 시작해서 커버할 수 있는 지점 체크
                    this_friend = weak[idx] + friend
                    
                    while idx < len(weak) and weak[idx] <= this_friend:
                        idx += 1
                    
                    if idx == start + len(weak) // 2:
                        return cnt
    return -1