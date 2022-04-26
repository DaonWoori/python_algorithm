# 소수 구하기

M, N = map(int, input().split())

# 에라토스테네스의 체
a = [False, False] + [True] * (N - 1)

p = []
for i in range(2, N+1):
  if a[i]:
    p.append(i) # 소수 담기
    for j in range(i*2, N+1, i):
      a[j] = False

for num in p:
  if num >= M:
    print(num)
