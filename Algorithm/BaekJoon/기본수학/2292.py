# 벌집

N = int(input()) # 입력

n = 1

while True:
    if n == 1:
        bn = 1
    else:
        # 등차수열 법칙 활용
        # bn = b1 + a1 + a2 + ... + an-1 = b1 + sn-1
        bn = 1 + 3 * (n - 1)**2 + 3 * (n - 1)

    if bn >= N:
        print(n)
        break
    n += 1
