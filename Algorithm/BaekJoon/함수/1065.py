# 한수
def hansu(num):
  cnt = 0
  if num <= 99:
    cnt += num
  else:
    cnt = 99
    for i in range(100, num + 1):
      nums = list(map(int, str(i)))
      if nums[0] - nums[1] == nums[1] - nums[2]:
        cnt += 1

  return cnt

N = int(input())
count = hansu(N)
print(count)

