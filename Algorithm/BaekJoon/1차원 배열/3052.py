# 나머지
import sys

remainder_set = set()

for _ in range(10):
  n = int(sys.stdin.readline())
  remainder_set.add(n % 42)

print(len(remainder_set))
