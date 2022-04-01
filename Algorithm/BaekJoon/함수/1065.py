# 한수
def hansu(num):
  cnt = 0
  if num <= 99:
    cnt += num
  else:
    cnt = 99
    for i in range(100, num + 1):
      hund = (i//100)
      ten = ((i%100)//10)
      one = ((i%100)%10)

      if hund - ten == ten - one:
        cnt += 1

  return cnt

N = int(input())
count = hansu(N)
print(count)

