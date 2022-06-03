# 0~9로 이루어진 문자열 입력
S = input()

result = 0

for i in S:
  n = int(i)
  if result == 0:
    result += n
    continue
  if n <= 1:
    result += n
  else:
    result *= n

print(result)
