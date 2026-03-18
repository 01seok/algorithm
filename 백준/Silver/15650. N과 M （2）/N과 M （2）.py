N, M = map(int, input().split())
seq = []

def backtracking(start):
    if len(seq) == M:
        print(*seq)
        return

    for i in range(start, N+1):
        seq.append(i)
        backtracking(i+1)
        seq.pop()


backtracking(1)