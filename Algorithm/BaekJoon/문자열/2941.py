# 크로아티아 알파벳

words = input()
cro_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for c in cro_list:
    words = words.replace(c, '.')
print(len(words))
