# 최댓값 

## 코드1
import sys

max_num = [0, 0]

for i in range(9):
  n = int(sys.stdin.readline())
  
  if max_num[1] < n:
    max_num[0] = i + 1
    max_num[1] = n

print(max_num[1], max_num[0], sep='\n')

## 코드2
import sys

num_li = []

for i in range(9):
  n = int(sys.stdin.readline())
  num_li.append(n)

print(max(num_li), num_li.index(max(num_li)) + 1, sep='\n')
