# 직사각형에서 탈출

import sys

x, y, w, h = map(int, sys.stdin.readline().split())

# 원점까지 x좌표 거리, 원점까지 y좌표 거리, 오른쪽 꼭짓점까지 x좌표 거리, 오른쪽 꼭짓점까지 y좌표 거리
distance_list = [x, y, w-x, h-y] 

print(min(distance_list))
