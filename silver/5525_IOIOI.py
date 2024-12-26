import sys
from collections import defaultdict

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
P_N = ["I" for _ in range(N+1)]
P_N = "O".join(P_N)
P_N_size = len(P_N)


M = int(sys.stdin.readline()) #S의 길이
S = sys.stdin.readline()

counter = defaultdict(int)

for i in range(0, M-P_N_size+1):
    counter[S[i:i+P_N_size]] += 1

print(counter[P_N])



# what
# N+1개의 I와 N개의 O가 교대로 나오는 문자열을 P_N이라고함
# 문자열 S가 주어졌을 때, P_N이 몇 군데 포함되어 있는지 구하라

# How
# 해시테이블에 슬라이딩 윈도우 범위 만큼의 문자열 개수를 저장

# 주의할 것
# S는 I,O가 교대로 반드시 나오는 것은 아님
# 위와 같은 방법으로 풀면 서브테스크만 만족