# Dynamic Programming

### Dynamic Programming이란?
> 복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 방법을 말한다. 한 번 계산한 결과를 재활용하는 방식
> by wikipedia

### Dynamic Programming 조건
1. 최적 부분 구조(Optimal Substructure): 부분 문제들의 최적의 답을 이용해서 기존 문제의 최적의 답을 구할 수 있다는 것
  
     ex) 피보나치 수열: fib(5)는 fib(4)와 fib(3)의 최적의 답으로 구할 수 있음.

2. 중복되는 부분 문제(Overlapping Subproblems) -> Dynamic Programming으로 문제 해결!

### Dynamic Programming 구현 방법
1. Memoization
2. Tabulation
