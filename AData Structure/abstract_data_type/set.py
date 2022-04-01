# 비어있는 set 정의
finished_classses = set()

# 데이터 저장
finished_classses.add("자료 구조")
finished_classses.add("알고리즘")
finished_classses.add("프로그래밍 기초")
finished_classses.add("인터렉티브 웹")
finished_classses.add("데이터 사이언스")

print(finished_classses) # 세트 출력

# 중복 데이터 저장 시도
finished_classses.add("자료 구조")
finished_classses.add("알고리즘")

print(finished_classses) # 세트 출력

# 데이터 탐색
print("컴퓨터 개론" in finished_classses)
print("자료 구조" in finished_classses)

# 데이터 삭제
finished_classses.remove("자료 구조")
finished_classses.remove("알고리즘")

print(finished_classses) # 세트 출력
