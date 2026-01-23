from itertools import permutations

def solution(numbers):

    # 소수 판별 함수
    def is_prime(num):

        if num < 2:
            return False

        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                return False
        
        return True


    # 모든 숫자 조합 만들기
    all_nums = set()

    # 한 자리 숫자부터 numbers 배열 길이만큼 까지 만들 수 있음
    for i in range(1, len(numbers)+1):
        # 순열
        for perm in permutations(numbers, i):
            num = int(''.join(perm))
            all_nums.add(num)

    # 소수가 몇 개인지 count
    cnt = 0
    for num in all_nums:
        if is_prime(num):
            cnt += 1
    
    return cnt
