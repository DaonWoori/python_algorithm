# 소수

M = int(input())
N = int(input())

prime_number = []

for i in range(M, N+1):
  clk = 0
  if i == 1:
    clk = 1
  for j in range(2, i):
    if i % j == 0:
      clk = 1
      break
  if clk == 0:
    prime_number.append(i)

if prime_number:
  print(sum(prime_number))
  print(min(prime_number))
else:
  print(-1)
