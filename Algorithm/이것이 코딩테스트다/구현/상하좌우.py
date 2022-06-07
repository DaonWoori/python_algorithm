import sys

N = int(sys.stdin.readline())
direct = list(sys.stdin.readline().split())

x = 1
y = 1

for d in direct:
  if d == 'R':
    if x < N:
      x += 1
  elif d == 'L':
    if x > 1:
      x -= 1
  elif d == 'U':
    if y > 1:
      y -= 1
  else:
    if y < N:
      y += 1

print(y, x)

