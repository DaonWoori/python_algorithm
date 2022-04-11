# 손익분기점
import sys

# A: 고정비, B: 가변 비용, C: 판매 비용
A, B, C = list(map(int, sys.stdin.readline().split()))

# 손익분기점이 존재하지 않는 경우
if B >= C:
    print(-1)
else:
    print(A // (C - B) + 1)
