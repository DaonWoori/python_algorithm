# 재귀함수가 뭔가요?

str_1 = '"재귀함수가 뭔가요?"'
str_2 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
str_3 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
str_4 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
str_5 = '"재귀함수는 자기 자신을 호출하는 함수라네"'
str_6 = '라고 답변하였지.'

def auto_reply(num):
  bar = "____" * (N - num)
  print(bar + str_1)
  if num == 0:
    print(bar + str_5)
    print(bar+ str_6)
    return 
    
  print(bar + str_2)
  print(bar + str_3)
  print(bar + str_4)
  auto_reply(num - 1)
  print(bar + str_6)

N = int(input())

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
auto_reply(N)
