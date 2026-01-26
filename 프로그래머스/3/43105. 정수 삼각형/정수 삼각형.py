def solution(triangle):

    # 밑에서 두 번쨰 줄부터 (r+1, c) or (r+1, c+1) 중에 큰거 더하면서 올라가기

    # 행은 올라가면서
    for r in range(len(triangle)-2, -1, -1):
        # 아래 숫자 뭐있는지 보면서 올라가기
        for c in range(len(triangle[r])):
            triangle[r][c] += max(triangle[r+1][c], triangle[r+1][c+1])

    return triangle[0][0]