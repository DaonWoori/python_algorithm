# 셀프 넘버

n = 0
END_NUM = 10000
dn = []

# 1 ~ End_num까지 활용해서 dn을 구해준 후 리스트에 넣어줌
for i in range(1, END_NUM+1):
    num_list = list(map(int, str(i)))
    sum_num = sum(num_list) + i
    dn.append(sum_num)

# dn 리스트에 들어있지 않은 값이 셀프넘버이므로 
for i in range(1, END_NUM+1):
    if i not in dn:
        print(i)
