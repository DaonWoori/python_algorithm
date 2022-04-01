# 곱셈
A = int(input())
B = int(input())

num1 = A * (B % 10)
num2 = A * ((B % 100) // 10)
num3 = A * (B // 100)
result = A * B

print(num1, num2, num3, result, sep='\n')
