import sys

n = int(sys.stdin.readline())
people = []
for _ in range(n):
    people.append(list(map(int, sys.stdin.readline().split())))

ranks = []
for i in range(n):
    rank = 1
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    ranks.append(rank)

print(*ranks)