'''
세그먼트 트리 : 특정 구간 최솟값, 최댓값 트리형태로 미리 구해두고 빠르게 구하는 자료구조
리프 노드에 원래 데이터 값들이 전부 들어가고, 부모 노드는 자식노드들 중 더 작은 값 or 더 큰 값을 담아서 저장
= 미리 구간별 승자 계산해서 저장해두는 방식

트리는 리스트로 만들어두고 포화 이진 트리 형태로 만들어두기 (4 * 전체 개수)
이 때 구간을 절반으로 쪼개서 비교하는 분할 정복 사용하기 !
'''

import sys
sys.setrecursionlimit(10**5) # 재귀 깊이 제한 해제
input = sys.stdin.readline

N, M = map(int, input().split())

# 비교할 숫자 리스트 입력
arr = []
for _ in range(N):
    arr.append(int(input()))


# 숫자들 비교할 수 있는 트리 생성
# 포화 이진 트리 (max 노드 개수)로 잡고 트리 생성
min_tree = [0] * (4 * N)    # 최솟값 구할 트리
max_tree = [0] * (4 * N)    # 최댓값 구할 트리

# 토너먼트 대진표 미리 채우기
# node : 현재 트리 노드 번호
# start, end : 현재 노드가 담당해서 비교할 범위
def init(node, start, end):

    # 리프노드(끝까지 가서 더이상 내려갈 수 없으면)까지 갔다면 거기 있는 값이 최솟값, 최댓값이니 종료
    if start == end:
        min_tree[node] = arr[start]
        max_tree[node] = arr[start]
        return

    # 분할 정복
    mid = (start + end) // 2

    # 왼쪽 자식과 오른쪽 자식, 양쪽으로 뻗어나가면서 리프노드까지 비교해나가기
    init(node * 2, start, mid)
    init(node * 2 + 1, mid + 1, end)

    # 최종 결과 : 좌 우 중 보고 더 작은 수, 더 큰 수 기록하기
    min_tree[node] = min(min_tree[node * 2], min_tree[node * 2 + 1])
    max_tree[node] = max(max_tree[node * 2], max_tree[node * 2 + 1])

# 문제에서 요구하는 구간에서 최솟값 구하는 함수 (left, right가 입력에서 요구하는 최솟값, 최댓값 구하는 구간)
def find_min(node, start, end, left,right):

    # 범위가 안 겹치는 경우 (볼 필요 없는 구간이므로 큰 수로 초기화해버리기, 어차피 범위 겹칠 때 최솟값으로 갱신될 것임)
    if left > end or right < start:
        return float('inf')
    
    # 범위가 완전 겹치는 경우엔 저장되어있는 값 바로 return
    if left <= start and end <= right:
        return min_tree[node]
    
    # 걸쳐있을 때, 좌 우 모두 확인해보고 더 작은 값 가져오기
    mid = (start + end) // 2
    return min(find_min(node * 2, start, mid, left, right),
               find_min(node * 2 + 1, mid + 1, end, left, right))

def find_max(node, start, end, left, right):
    
    # 범위 x
    if left > end or right < start:
        return 0
    
    # 범위 완전 포함
    if left <= start and end <= right:
        return max_tree[node]
    
    # 부분 포함
    mid = (start + end) // 2
    return max(find_max(node * 2, start, mid, left, right),
               find_max(node * 2 + 1, mid + 1, end, left, right))

# 실제 트리 생성
# 루트 노드는 1번, 0 ~ N-1번까지 노드 생성
init(1, 0, N-1)

# 입력값들 처리
for _ in range(M):
    a, b = map(int, input().split())
    # idx = -1처리
    print(find_min(1, 0, N-1, a-1, b-1), find_max(1, 0 , N-1, a-1, b-1))