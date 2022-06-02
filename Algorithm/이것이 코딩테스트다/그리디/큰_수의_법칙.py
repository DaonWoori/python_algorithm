# 큰 수의 법칙

N, M, K = map(int, input().split())

nums_list = list(map(int, input().split()))

# 입력받은 수들 정렬하기
nums_list.sort()

# 가장 큰 수
first = nums_list[N - 1]

# 두번째로 큰 수 
second = nums_list[N - 2]

sum = 0
count = K

for _ in range(M):
  if count:
    sum += first
    count -= 1
  else:
    sum += second
    count = K

print(sum)
