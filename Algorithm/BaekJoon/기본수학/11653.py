# 소인수분해

N = int(input())

num = N
i = 2

while num != 1:
  if num % i == 0:
    print(i)
    num = num // i
  else:
    i += 1
