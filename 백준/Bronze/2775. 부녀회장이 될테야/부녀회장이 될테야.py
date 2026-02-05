import sys

input_data = sys.stdin.read().split()
if input_data:
    t = int(input_data[0])
    curr = 1

    for _ in range(t):
        k = int(input_data[curr])
        n = int(input_data[curr + 1])
        curr += 2

        # 0층의 i호에는 i명이 살고 있는 상태로 초기화합니다.
        people = [i for i in range(1, n + 1)]

        # k번만큼 층을 올리며 각 호수의 인원수를 누적합으로 갱신합니다.
        for _ in range(k):
            for j in range(1, n):
                people[j] += people[j - 1]

        # 최종적으로 k층 n호의 거주민 수를 출력합니다.
        print(people[n - 1])