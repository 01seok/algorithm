from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])

    # 창고 외부에서 BFS를 시작할 수 있게 만들기
    board = [["."] * (m + 2)]

    for row in storage:
        board.append(["."] + list(row) + ["."])

    board.append(["."] * (m + 2))

    rows = n + 2
    cols = m + 2

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 현재 창고 외부와 연결된 빈 공간을 BFS로 찾는 함수
    def get_outside():
        visited = [[False] * cols for _ in range(rows)]
        q = deque()

        q.append((0, 0))
        visited[0][0] = True

        while q:
            x, y = q.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                    continue

                if visited[nx][ny]:
                    continue

                # 빈 공간만 이동 가능
                if board[nx][ny] == ".":
                    visited[nx][ny] = True
                    q.append((nx, ny))

        return visited

    for request in requests:
        target = request[0]

        # 크레인 요청
        # 요청 길이가 2이면 해당 종류 컨테이너를 전부 제거
        if len(request) == 2:
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if board[i][j] == target:
                        board[i][j] = "."

        # 지게차 요청
        # 외부와 맞닿아 있는 target 컨테이너만 제거
        else:
            outside = get_outside()
            remove_list = []

            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if board[i][j] != target:
                        continue

                    # 상하좌우 중 하나라도 외부와 연결된 빈 공간이면 접근 가능
                    for d in range(4):
                        ni = i + dx[d]
                        nj = j + dy[d]

                        if outside[ni][nj]:
                            remove_list.append((i, j))
                            break

            # 같은 요청 안에서는 먼저 제거 대상을 전부 정한 뒤 한꺼번에 제거
            for x, y in remove_list:
                board[x][y] = "."

    answer = 0

    # padding 제외하고 남은 컨테이너 개수 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i][j] != ".":
                answer += 1

    return answer