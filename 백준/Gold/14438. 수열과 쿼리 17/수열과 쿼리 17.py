import sys
import math

input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))

# 한 버킷의 사이즈, 버킷 개수, 초기 값 세팅
bucket_size = int(math.sqrt(N)+1)
bucket_cnt = (N // bucket_size)
bucket = [float('inf')] * bucket_size

# 초기 버킷 계산
# 각 원소가 어느 버킷에 소속되어있는지 확인
# 그 버킷의 최솟 값 갱신
for i in range(1, N+1):
    # 몇 번째 버킷에 들어가는지
    bucket_idx = i // bucket_size
    bucket[bucket_idx] = min(bucket[bucket_idx], arr[i])


# 1번 쿼리, 업데이트 함수
# 값 바꾸기 + 해당 버킷에서 최솟 값 갱신

def update(idx, val):
    arr[idx] = val
    bucket_idx = idx // bucket_size

    # 이 버킷 시작 값과 끝 인덱스 계산
    start = bucket_idx * bucket_size
    end = min(start+ bucket_size, N+1)

    # bucket 초기화하고 다시 계산
    bucket[bucket_idx] = float('inf')
    for i in range(start, end):
        if i > 0:
            bucket[bucket_idx] = min(bucket[bucket_idx], arr[i])

def query(left, right):

    result = float('inf')

    # 두 수가 어느 버킷에 속하는지 확인하기
    left_bucket = left // bucket_size
    right_bucket = right // bucket_size

    # 같은 버킷에 소속되어있는 case
    if left_bucket == right_bucket:
        for i in range(left, right+1):
            result = min(result, arr[i])

        return result

    # 다른 버킷들에 걸쳐있는 경우

    # left가 속한 버킷에서 left부터 그 버킷 끝까지의 값들 확인
    for i in range(left, (left_bucket + 1) * bucket_size):
        if i <= N:
            result = min(result, arr[i])

    # 중간에 있는 버킷들은 이미 계산되어있는 값들 사용
    for mid in range(left_bucket+1, right_bucket):
        result = min(result, bucket[mid])

    # 오른쪽 버킷 시작부터 right까지 확인
    for j in range(right_bucket * bucket_size, right+1):
        if j <= N:
            result = min(result, arr[j])

    return result


# query 개수
M = int(input())
for _ in range(M):
    cmd, a, b = map(int, input().split())
    
    if cmd == 1:
        update(a, b)
    
    else:
        print(query(a, b))