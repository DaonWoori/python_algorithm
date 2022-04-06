# 알파벳 찾기
import string
small_l = string.ascii_lowercase
# alphabet = list(range(97,123))  # 아스키코드 숫자 범위

input_st = input()

for s in small_l:
    idx = input_st.find(s)
    print(idx, end=' ')
