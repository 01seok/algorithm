N, M = map(int, input().split())
seq = []
visited = [False] * (N+1)

def backtracking():
    if len(seq) == M:
        print(*seq)
        return 
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            seq.append(i)
            
            backtracking()
            seq.pop()
            visited[i] = False

backtracking()