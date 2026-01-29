import math
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    a = int(input_data[0])
    b = int(input_data[1])
    
    greatest_common_divisor = math.gcd(a, b)
    least_common_multiple = (a * b) // greatest_common_divisor
    
    print(greatest_common_divisor)
    print(least_common_multiple)

solve()