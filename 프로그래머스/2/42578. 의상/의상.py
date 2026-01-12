# 해시

# 알몸 안됨
# 단 한개라도 입으면 되니까 종류별로 갯수 + 안 입음 경우의 수로 생각하기

# 입력은 의상 이름, 의상 종류
# 의상 종류 당 몇 벌인지만 파악하면 됨

def solution(clothes):

    # 종류별로 개수 저장해둘 딕셔너리
    closet = {}

    for cloth in clothes:
        # cloth는 (의상 이름, 의상종류)로 들어옴
        category = cloth[1]

        # 해시에 반영
        if category in closet:
            closet[category] += 1

        else:
            closet[category] = 1

    # 경우의 수 계산 : 딕셔너리 안의 값들 + 1 (안 입는거) 해서 곱해주면 됨
    answer = 1 # 곱해야하니까 1부터 시작
    
    for num in closet.values():
        answer *= (num + 1)
        
    # 알몸의 경우 1개 빼고
    return answer - 1