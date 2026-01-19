def solution(array, commands):
    answer = []

    # i, j, k를 하나씩 꺼내서 처리
    for command in commands:
        i, j, k = command

        # 자르기, 인덱스 i-1
        sliced_arr = array[i - 1:j]

        # 정렬
        sorted_arr = sorted(sliced_arr)

        # k번째 수 뽑기
        kth_num = sorted_arr[k - 1]

        answer.append(kth_num)

    return answer