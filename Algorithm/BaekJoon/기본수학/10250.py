# ACM 호텔
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    floor = N % H
    room = N // H + 1

    if floor == 0:
        floor = H
        room = room - 1

    if room < 10:
        room = "0" + str(room)

    print(f"{floor}{room}") # print(floor * 100 + room)
