# 숫자의 개수
import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

num_st = str(A * B * C)

for i in "0123456789":
  print(num_st.count(i))
