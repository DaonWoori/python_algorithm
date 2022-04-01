# 더하기 사이클
import sys

N = sys.stdin.readline().strip().zfill(2)
num = N

count = 0
while True:
  sum = str(int(num[0]) + int(num[1])).zfill(2)
  num = num[1] + sum[1]
  count += 1

  if num == N:
    break
  
print(count)
