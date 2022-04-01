# 평균은 넘겠지
import sys

C = int(sys.stdin.readline())

for i in range(C):
  score_li = list(map(int, sys.stdin.readline().split()))
  mean_score = sum(score_li[1:]) / score_li[0]
  filter_count = list(filter(lambda x : x > mean_score, score_li[1:]))
  print(f"{len(filter_count) / score_li[0] * 100:.3f}%")
