# 단어 공부
import string

upper_list = string.ascii_uppercase # 대문자 리스트
upper_count = [0] * len(upper_list)

# 입력: 대소문자로 이루어진 단어
word = input()

# 대문자로 모두 변환
word = word.upper()
count = 0

# 단어에 사용된 알파벳의 개수 세기
for s in word:
    idx = upper_list.index(s)
    upper_count[idx] += 1

max = max(upper_count)
max_idx = upper_count.index(max)

list = upper_count.copy()
del list[max_idx]

if upper_count[max_idx] not in list:
    print(upper_list[max_idx])
else:
    print("?")

