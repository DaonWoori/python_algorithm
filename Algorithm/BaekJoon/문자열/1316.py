# 그룹 단어 체커
N = int(input())
count = 0

for i in range(N):
    words = input()
    ex_list = []
    temp = 1
    for i, s in enumerate(words):
        if s in ex_list:
            temp = 0
            break
        else:
            if i != len(words)-1 and words[i] == words[i + 1]:
                continue
            else:
                ex_list.append(s)
    if temp == 1:
        count += 1

print(count)
