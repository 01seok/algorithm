N, M = map(int, input().split())
seq = []
visited = [False] * (N+1)

def is_up(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False

    return True

def backtracking():
    if len(seq) == M:
        print(*seq)
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            seq.append(i)
            if is_up(seq):

                backtracking()
            seq.pop()
            visited[i] = False

backtracking()