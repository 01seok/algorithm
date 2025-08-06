word = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
for ch in word:
    for i in range(len(dial)):
        if ch in dial[i]:
            time += i + 3
            break
print(time)