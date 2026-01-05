def solution(k, dungeons):
    answer = -1

    # N = 던전 갯수
    N = len(dungeons)

    visited = [False] * N

    def dfs(cur_k, cnt):
        nonlocal answer

        # 최대 개수 던전 돌고있으면 갱신하고
        if cnt > answer:
            answer = cnt

        # 모든 던전 보면서 갈 수 있는지 확인
        for i in range(N):
            # 던전 입장 컷 피로도와 실제 소모되는 피로도
            min_require, real_require = dungeons[i]

            if not visited[i] and cur_k >= min_require:
                visited[i] = True
                dfs(cur_k - real_require, cnt + 1)

                # 원상 복구
                visited[i] = False
    dfs(k, 0)

    return answer