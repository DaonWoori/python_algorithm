# 카드의 행의 개수와 열의 개수 입력
N, M = map(int, input().split())

# 카드 행에서 최소값 리스트
min_list = []

for _ in range(N):
  num_list = list(map(int, input().split()))
  min_list.append(min(num_list))

print(max(min_list))

