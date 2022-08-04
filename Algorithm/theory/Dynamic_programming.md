# Dynamic Programming

### Dynamic Programming이란?
> 복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 방법을 말한다.
> by wikipedia

### Dynamic Programming 조건
1. 최적 부분 구조(Optimal Substructure): 부분 문제들의 최적의 답을 이용해서 기존 문제의 최적의 답을 구할 수 있다는 것
  
     ex) 피보나치 수열: fib(5)는 fib(4)와 fib(3)의 최적의 답으로 구할 수 있음.

2. 중복되는 부분 문제(Overlapping Subproblems) -> Dynamic Programming으로 문제 해결!

### Dynamic Programming 구현 방법
1. Memoization by 재귀: 중복되는 계산은 한번만 계산 후 메모해놓는 방식 -> **하향식 접근(Top-Down)** 
   > 단점: 재귀를 많이 사용하면 call stack이 쌓여 과부하 발생
2. Tabulation by 반복문: 중복되는 것을 먼저 계산하는 방식 -> **상향식 접근(Bottom-Up)** 
   > 단점: 표를 하나씩 채워야 하므로 n번째 값을 구하기 위해서 처음부터 끝까지 계산해야하므로 낭비 발생 

