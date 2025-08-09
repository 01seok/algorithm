import sys

def roll_dice(dice, command):
    # dice = [윗면 , 아랫면, 동, 서, 남, 북]

    # 원본 주사위 복사해서 사용
    new_dice = dice[:]

    # 동쪽으로 굴리면
    if command == 1:
        # 윗면(0) -> 서쪽(3), 서쪽(3) -> 아랫면(1), 아랫면(1) -> 동쪽(2), 동쪽(2) -> 윗면(0)
        new_dice[0], new_dice[1], new_dice[2], new_dice[3] = dice[3], dice[2], dice[0], dice[1]
    # 서쪽으로 굴리기
    elif command == 2:
        # 윗면(0) -> 동쪽(2), 동쪽(2) -> 아랫면(1), 아랫면(1) -> 서쪽(3), 서쪽(3) -> 윗면(0)
        new_dice[0], new_dice[1], new_dice[2], new_dice[3] = dice[2], dice[3], dice[1], dice[0]
    # 북쪽으로 굴리기
    elif command == 3:
        # 윗면(0) -> 남쪽(5), 남쪽(5) -> 아랫면(1), 아랫면(1) -> 북쪽(4), 북쪽(4) -> 윗면(0)
        new_dice[0], new_dice[1], new_dice[4], new_dice[5] = dice[5], dice[4], dice[0], dice[1]
    # 남쪽으로 굴리기
    elif command == 4:
        # 윗면(0) -> 북쪽(4), 북쪽(4) -> 아랫면(1), 아랫면(1) -> 남쪽(5), 남쪽(5) -> 윗면(0)
        new_dice[0], new_dice[1], new_dice[4], new_dice[5] = dice[4], dice[5], dice[1], dice[0]

    return new_dice

N, M, x, y, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
commands = list(map(int, sys.stdin.readline().split()))

dice = [0, 0, 0, 0, 0, 0]

# index 0은 쓰지않고 동서북남 (문제에서 주어진 명령의 순서대로)
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

for command in commands:
    nr, nc = x +dr[command], y + dc[command]

    if 0 <= nr < N and 0 <= nc < M:
        dice = roll_dice(dice, command)
        x, y = nr, nc

        bottom_value = dice[1]
        if board[x][y] == 0:
            board[x][y] = bottom_value
        else:
            dice[1] = board[x][y]
            board[x][y] = 0

        print(dice[0])