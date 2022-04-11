# 분수 찾기
X = int(input())
b1 = 1

for i in range(1, X + 1):
    bi = int(b1 + ((i - 1) * (i + 2)) / 2)
    if bi >= X:
        start = int(b1 + ((i - 2) * (i + 1)) / 2) + 1
        if i % 2 == 0: # 짝수그룹 -> 분모가 큼
            deno = i - (X - start)
            numer = i - (bi - X)
        else: # 홀수 그룹 -> 분자가 큼
            deno = i - (bi - X)
            numer = i - (X - start)
        break
print(f"{numer}/{deno}")
