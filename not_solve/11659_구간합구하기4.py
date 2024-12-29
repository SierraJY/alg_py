import sys

sys.stdin = open('input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())

l = [0] + list(map(int, sys.stdin.readline().split()))
s_l = [0]
for i in range(1, N+1):
    s_l.append(s_l[i-1] + l[i])

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(s_l[e] - s_l[s-1])


# 주의할 것
# 원본 matrix와 구간합 matrix 초기 설정