# 숫자의 합
import sys
N = int(sys.stdin.readline())
nums = sys.stdin.readline().strip()

print(sum(list(map(int, nums))))
