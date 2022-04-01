from collections import deque
# deque(doubly-ended-queue): 맨 앞과 뒤에 데이터를 삽입하고 삭제할 수 있게 해주는 자료형

stack = deque()

# 스택 맨 끝에 데이터 추가
stack.append("T")
stack.append("a")
stack.append("e")
stack.append("h")
stack.append("o")

print(stack) # 스택 출력

# 맨 끝 데이터 접근
print(stack[-1])

# 맨 끝 데이터 삭제
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack) # 스택 출력
