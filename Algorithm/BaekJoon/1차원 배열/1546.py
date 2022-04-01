# 평균
import sys

N = int(sys.stdin.readline())
score_li = list(map(int, sys.stdin.readline().split()))

new_score = [s / max(score_li) * 100 for s in score_li]

print(sum(new_score) / N)
