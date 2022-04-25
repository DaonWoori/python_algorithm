# 소수 찾기

def prime_number(num):
    if num == 1:
        return 0
    clk = 1
    for i in range(2, num):
        if num % i == 0:
            clk = 0
            break
    return clk


N = int(input())
nums = list(map(int, input().split()))

count = 0
for num in nums:
    count += prime_number(num)

print(count)
