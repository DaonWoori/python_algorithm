"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
This code is available at https://nostarch.com/big-book-small-python-programming
A version of this game is featured in the book, "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3 # 맞춰야 할 숫자의 자릿수
MAX_GUESSES = 10

def main():
    print(f'''
    I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:       That means:
        Pico          One digit is correct but in the wrong position.
        Fermi         One digit is correct and in the right position.
        Baggles       No digit is correct.  
    ''')

    # main game
    while True:
        # 사용자가 예측해야 할 비밀번호 지정
        secretNum = getSecretNum()

        print('Start GAME!!!!!!!!!!')

        print("I have thought up a number.")
        print(f'You have {MAX_GUESSES} guesses to get.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # 유효한 예측값을 입력할 때까지 계속 루프를 돈다.
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}: ")
                guess = input('> ')
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of gueese.')
                print(f'The answer was {secretNum}')

        # 다시 게임을 하고 싶은지 물어봄
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thaks for playing!')

def getSecretNum():
    # NUM_DIGITS개의 임의 숫자로 구성된 문자열 변환
    numbers = list('0123456789')
    random.shuffle(numbers)

    # 비밀번호를 뽑기 위해 리스트의 처음부터 NUM_DIGITS의 자리까지 수를 얻는다.
    secretnum = ""
    for i in range(NUM_DIGITS):
        secretnum += str(numbers[i])
    
    return secretnum

def getClues(guess, secretNum):
    """비밀번호에 대한 단서인 pico, fermi, bagels로 구성된 문자열 반환"""
    if guess == secretNum:
        return 'You got it'
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Baggles'
    
    else:
        # 힌트를 알파벳 순으로 정렬하여 힌트의 순서가 힌트가 되지 않도록 한다.
        clues.sort()

        return ' '.join(clues)

if __name__ == "__main__": # 모듈과 메인을 구분하기 위해 사용
    main()
