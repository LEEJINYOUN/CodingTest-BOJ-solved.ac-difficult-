#자연수 N과 정수 K가 주어졌을 때 이항계수 N K (nCk)를 구하는 프로그램을 작성하시오

import sys

N, K = map(int, sys.stdin.readline().split())

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(N) // (factorial(N - K) * factorial(K))) # 조합 공식 nCk = n! / (n - k)! * k!