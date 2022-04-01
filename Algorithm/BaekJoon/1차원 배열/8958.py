# OX 퀴즈
import sys

N = int(sys.stdin.readline())

for i in range(N):
  ox_str = sys.stdin.readline().strip()
  score = 0
  weight = 0
  for s in ox_str:
    if s == 'O':
      weight += 1
    else:
      weight = 0
    score += weight
  print(score)
