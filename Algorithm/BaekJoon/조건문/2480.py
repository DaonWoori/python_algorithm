num1, num2, num3 = map(int, input().split())

# 세 개 모두 같은 경우
if num1 == num2 and num1 == num3 and num2 == num3:
    reward = 10000 + num1 * 1000
# 모두 다른 경우
elif num1 != num2 and num1 != num3 and num2 != num3:
    reward = max(num1, num2, num3) * 100
# 두 개만 같은 경우
else:
    if num1 == num2:
        reward = 1000 + num1 * 100
    elif num1 == num3:
        reward = 1000 + num1 * 100
    else:
        reward = 1000 + num2 * 100

print(reward)

# tip
# set 자료형을 활용해볼 것!

