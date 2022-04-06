# 알파벳 찾기
import string
small_l = string.ascii_lowercase

input_st = input()

for s in small_l:
    idx = input_st.find(s)
    print(idx, end=' ')
