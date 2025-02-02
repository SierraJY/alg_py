import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())

def hanoi(prev, buff, next, n):
    global call_cnt
    if n == 1:
        print(prev, next)
    else:
        hanoi(prev, next, buff, n-1)
        hanoi(prev, buff, next,1)
        hanoi(buff, prev, next, n - 1)

print(2**(N) - 1)
if N <= 20 :
    hanoi(1, 2, 3, N)

# 주의할 것
# 하노이탑에서 재귀 호출횟수 카운팅은 어떻게 해야할까?
# 규칙이 있지 않을까?

# 재귀는
# 큰 문제에서 -> 작은 문제로
