import sys
s=sys.stdin.readline().strip()
print(''.join(sorted(s, reverse=True)))