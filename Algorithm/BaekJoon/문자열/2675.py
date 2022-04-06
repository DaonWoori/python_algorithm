# 문자열 반복
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    R, S = sys.stdin.readline().split()

    for s in S:
        print(s * int(R), end='')
    print()
