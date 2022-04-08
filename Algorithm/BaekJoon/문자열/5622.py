# 다이얼

dial = {
    "ABC": 2,
    "DEF": 3,
    "GHI": 4,
    "JKL": 5,
    "MNO": 6,
    "PQRS": 7,
    "TUV": 8,
    "WXYZ": 9
}
word = input()

time = 0
for w in word:
    for key in dial:
        if w in key:
            time += dial[key] + 1

print(time)
