def solution(message, spoiler_ranges):
    words = []

    # message에서 단어의 문자열, 시작 인덱스, 끝 인덱스 추출
    start = 0
    for i in range(len(message) + 1):
        if i == len(message) or message[i] == " ":
            words.append((message[start:i], start, i - 1))
            start = i + 1

    normal_words = set()
    spoiler_words = []

    range_idx = 0
    range_count = len(spoiler_ranges)

    # 각 단어가 스포 방지 구간과 겹치는지 확인
    for word, word_start, word_end in words:
        # 현재 단어보다 완전히 왼쪽에 있는 스포 구간은 넘김
        while range_idx < range_count and spoiler_ranges[range_idx][1] < word_start:
            range_idx += 1

        temp_idx = range_idx
        is_spoiler_word = False
        last_range_idx = -1

        # 현재 단어와 겹치는 스포 구간을 모두 확인
        while temp_idx < range_count and spoiler_ranges[temp_idx][0] <= word_end:
            is_spoiler_word = True
            last_range_idx = temp_idx
            temp_idx += 1

        if is_spoiler_word:
            # 이 단어는 last_range_idx 번째 스포 구간을 클릭했을 때
            # 단어 전체가 공개됨
            spoiler_words.append((last_range_idx, word_start, word))
        else:
            # 스포 방지 구간이 아닌 곳에 등장한 일반 단어
            normal_words.add(word)

    # 3. 스포 구간 클릭 순서대로 공개 단어 처리
    spoiler_words.sort()

    revealed_words = set()
    answer = 0

    for _, _, word in spoiler_words:
        # 일반 영역에 등장한 적 있으면 중요 단어 아님
        if word in normal_words:
            revealed_words.add(word)
            continue

        # 이전에 공개된 스포 방지 단어와 중복되면 중요 단어 아님
        if word in revealed_words:
            continue

        # 위 조건을 모두 통과하면 중요한 단어
        answer += 1
        revealed_words.add(word)

    return answer