import sys
from bisect import bisect_right

sys.stdin = open('input.txt', 'r')
N, K, T = map(int, sys.stdin.readline().split())
Q = list(map(lambda x: int(x), sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))

Q = [q % K for q in Q]  # 모든 원소를 K로 나눈 나머지로 변환
Q.sort()  # 정렬
current_add = 0  # 누적 합

for a in A:
    current_add = (current_add + a) % K  # 누적 합 갱신

    idx = bisect_right(Q, K - 1 - current_add)
    if idx == 0:  # 모든 값이 범위를 벗어나는 경우
        max_val = (Q[-1] + current_add) % K
    else:
        max_val = max((Q[idx - 1] + current_add) % K, (Q[-1] + current_add) % K)

    print(max_val, end = " ")

# 주의할 것
# 우선순위 큐 문제라도, 반드시 Heap을 사용하는 문제가 아닐 수 있음
# 우선순위 큐 != Heap

# 알게된 것
# 모듈로 연산의 연산 법칙(결합 , 분배)
# (((a + b) % k) + c) % k = (a + b + c)%k 임을 증명

# (a + b) % k
# (a % k + b % k) %k

# (((a + b) % k) + c) % k
# (((a + b) % k) % k +  c % k) % k
# (((a + b) % k) + c % k) % k
# (((a + b) + c) % k) % k
# ((a + b) + c)%k
# (a + b + c)%k