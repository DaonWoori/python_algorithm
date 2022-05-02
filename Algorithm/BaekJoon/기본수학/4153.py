# 직각삼각형

import sys

while True:
  points = list(map(int, sys.stdin.readline().split()))
  points.sort()

  if sum(points) == 0:
    break

  if points[0]**2 + points[1]**2 == points[2]**2:
    print("right")
  else:
    print("wrong")
  
