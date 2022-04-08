# 상수
import sys

num1, num2 = sys.stdin.readline().split()

r_num1 = int(num1[::-1])
r_num2 = int(num2[::-1])

if r_num1 > r_num2:
    print(r_num1)
else:
    print(r_num2)
