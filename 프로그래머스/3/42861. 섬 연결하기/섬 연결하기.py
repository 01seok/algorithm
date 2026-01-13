def solution(n, costs):
    # 부모 테이블 초기화
    parents = [i for i in range(n)]

    # find 함수 (경로 압축 적용)
    def find_set(x):
        if parents[x] != x:
            parents[x] = find_set(parents[x])
        return parents[x]

    # union 함수
    def union(x, y):
        root_x = find_set(x)
        root_y = find_set(y)
        
        # 번호가 작은 쪽으로 합치기
        if root_x < root_y:
            parents[root_y] = root_x
        else:
            parents[root_x] = root_y

    # 비용 기준 오름차순 정렬
    costs.sort(key=lambda x: x[2])

    total_cost = 0
    edge_cnt = 0

    # 간선 하나씩 확인하며 MST 구성
    for u, v, w in costs:
        if find_set(u) != find_set(v):
            union(u, v)
            total_cost += w
            edge_cnt += 1
            
            # 간선 n-1개 연결되면 조기 종료
            if edge_cnt == n - 1:
                break
                
    return total_cost