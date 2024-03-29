# Brute Force(완전 탐색)

### 완전 탐색이란?
> 해가 존재할 것으로 예상되는 모든 영역을 전체 탐색하는 방법

### 완전 탐색 알고리즘의 장점
1. 직관적이고 명확하다 -> 코드를 구현하기 쉬움
2. 답을 확실하게 찾을 수 있다

=> input이 엄청 크지 않는 경우, 효율적인 알고리즘이 될 수 있음.

### 완전 탐색 알고리즘의 종류
1. Brute Force 기법
> 반복문/조건문을 통해 가능한 모든 방법을 찾는 경우
2. 백트래킹(Backtracking) 기법
> 현재 상태에서 가능한 후보군으로 가치를 치며 탐색하는 알고리즘
3. 순열(Permutation)
> 서로 다른 n개의 원소에서 r개를 중복없이 순서에 상관있게 선택하는 혹은 나열하는 것으로 임의의 수열이 주어졌을 때 그것을 다른 순서로 연산하는 방법
4. 비트 마스크(Bit Mask)
> 2진수를 이용하는 방식으로 모든 경우의 수가 각각의 원소가 포함되거나, 포함되지 않는 두 가지 선택으로 구성되는 경우 유용
5. 재귀함수
6. DFS/BFS
