"""Bitmap Message, by Al Sweigart al@inventwithpython.com
Displays a text message according to the provided bitmap image.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, artistic"""

import sys # 파이썬 인터프리터가 제공하는 변수나 함수를 제어할 수 있는 방법 제공

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""

print("Bitmap Message")
print("Enter the message ti display with the bitmap.")
message = input('> ')

if message == '':
    sys.exit() # 프로그램 종료 함수

# 루프를 돌며 bitmap의 각 행을 반복한다.
for line in bitmap.splitlines(): # 문자열을 줄바꿈 기준으로 쪼개기
    # 루프를 돌며 행의 각 문자를 반복한다.
    for i, bit in enumerate(line):
        if bit == ' ':
            # bitmap의 해당 위치가 공백이므로 빈 공백을 출력
            print(' ', end='')
        else:
            # message의 문자를 출력
            print(message[i % len(message)], end='')
    print() # 줄을 바꾼다.
