# X보다 작은 수
import sys

N, X = map(int, sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))

for num in data:
  if num < X:
    print(num, end=" ")
