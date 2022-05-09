# 1이 될 때까지

N, K = map(int, input().split())

count = 0

while True:
  if N == 1:
    break

  if N % K:
    N -= 1
    count += 1
  else:
    N = N // K
    count += 1

print(count)
  
