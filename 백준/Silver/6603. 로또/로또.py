import sys
from itertools import combinations

while True:
    data = list(map(int, sys.stdin.readline().split()))
    
    if data[0] == 0:
        break
        
    k = data[0]
    nums = data[1:]
    
    for comb in combinations(nums, 6):
        print(*comb)
        
    print()