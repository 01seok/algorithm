from collections import deque

def solution(begin, target, words):

    # target을 만들 수 없으면
    if target not in words:
        return 0

    # 큐 안에 현재 단어와 현재까지 거쳐온 단계 수 넣기
    q = deque([(begin, 0)])

    # 한 번 거친 단어는 다시 방문할 필요 x
    visited = [False] * len(words)

    while q:
        cur_word, cnt = q.popleft()

        # 목표 단어 완성 되었으면 몇 번 걸렸는지 return
        if cur_word == target:
            return cnt

        for i in range(len(words)):
            if not visited[i]:

                diff_cnt = 0
                # 다른 글자 수 세어보기 (한 개의 알파벳만 바꿀 수 있으니까)
                for j in range(len(cur_word)):
                    # 서로 j번째 글자가 다르다면 다른 글자 수 + 1
                    if cur_word[j] != words[i][j]:
                        diff_cnt += 1


                if diff_cnt == 1:
                    visited[i] = True
                    # i번째 words 단어와 거쳐온 단계 수 + 1
                    q.append((words[i], cnt+1))
    return 0
