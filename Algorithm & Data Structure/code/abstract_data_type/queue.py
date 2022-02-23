from collections import deque
# deque(doubly-ended-queue): 맨 앞과 뒤에 데이터를 삽입하고 삭제할 수 있게 해주는 자료형

queue = deque()

# 큐의 맨 끝에 데이터 삽입
queue.append("태호")
queue.append("현승")
queue.append("지웅")
queue.append("동욱")
queue.append("신의")

print(queue) # 큐 출력

# 큐의 가장 앞 데이터에 접근
print(queue[0])

# 큐 맨 앞 데이터 삭제
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print(queue) # 큐 출력
