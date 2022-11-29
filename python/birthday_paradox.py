"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, math, simulation"""

import datetime, random

def getBirthdays(number_of_birthdays):
    """생일에 대한 임의의 날짜 객체들의 리스트 반환"""
    birthdays = []

    for _ in range(number_of_birthdays):
        # 년도는 중요하지 x
        start_of_year = datetime.date(2022, 1, 1)

        # 임의의 날짜 얻기
        random_number_of_days = datetime.timedelta(random.randint(0, 364)) # 기간을 표현
        birthday = start_of_year + random_number_of_days # 산술연산으로 날짜를 계산
        birthdays.append(birthday)

    return birthdays

def getMatch(birthdays):
    """생일 리스트에서 중복되는 생일 날짜 객체 반환"""
    if len(birthdays) == len(set(birthdays)):
        return None # 모든 생일이 다른 경우
    
    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a+1:]):
            if birthday_a == birthday_b:
                return birthday_a


def main():
    # 인트로 출력
    print("The birthday paradox shows")

    # 월 이름이 순서대로 있는 튜플
    MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    
    while True: # 사용자가 유효한 값을 입력할 때까지
        print('How many birthdays shall I generate? (Max 100)')
        response = input('> ')

        if response.isdecimal() and (0 < int(response) <= 100):
            numBDays = int(response)
            break
    
    print()

    # 생일을 생성하고 출력하기
    print('Here are', numBDays, 'birthdays: ')
    birthdays = getBirthdays(numBDays)
    for i, birthday in enumerate(birthdays):
        if i != 0:
            # 첫 번째 생일 이후부터 각 생일마다 콤마를 표시
            print(', ', end="")
        month_name = MONTHS[birthday.month - 1]
        date_text = '{} {}'.format(month_name, birthday.day)
        print(date_text, end='')
    print()
    print()

    # 두 생일이 서로 일치하는지 판단
    match = getMatch(birthdays)

    # 결과 출력하기
    print('In this simulation, ', end='')
    if match != None:
        month_name = MONTHS[birthday.month - 1]
        date_text = '{} {}'.format(month_name, birthday.day)
        print('multiple people have a birthday on', date_text)
    else:
        print('there are no matching birthdays.')

if __name__ == "__main__": # 모듈과 메인을 구분하기 위해 사용
    main()
