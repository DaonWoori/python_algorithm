# 좌표 입력
point = input()

# x좌표값(a,b,c,d,e,f,g,h)를 숫자값으로 변환
x = ord(point[0]) - 96
y = int(point[1])

count = 0
direct = [-1, 1]

for i in range(2):
  # 좌우로 먼저 움직이는 경우(x좌표)
  nx = x + 2 * direct[i]
  
  if nx >= 1 and nx <= 8:
    # 위아래로 움직이는 경우(y좌표)
    for j in range(2):
      ny = y + direct[j]
      if ny >= 1 and ny <= 8:
        print(f"좌우먼저: {nx}, {ny}")
        count += 1

  # 위아래로 먼저 움직이는 경우(y좌표)
  ny = y + 2 * direct[i]

  if ny >= 1 and ny <= 8:
    # 좌우로 움직이는 경우(x좌표)
    for j in range(2):
      nx = x + direct[j]
      if nx >= 1 and nx <= 8:
        print(f"위아래먼저: {nx}, {ny}")
        count +=1

print(count)
  

