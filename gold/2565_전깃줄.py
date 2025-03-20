import sys

sys.stdin = open(0, 'r')
input = sys.stdin.readline

N = int(input())

lines = []
for _ in range(N):
    A, B = map(int, input().split())
    lines.append((A,B))

lines.sort(key=lambda x:x[0])
dp = [1 for _ in range(N)]
for i in range(N):
    cur_line_b = lines[i][1]
    for j in range(i):
        if cur_line_b > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

# print(dp)
print(N-max(dp))

# 아이디어 & 알고리즘
# 전깃줄이 서로 교차하지 않게 하기 위해서 없애야하는 전깃줄 최소 개수?
# => 완탐(?)
    # 전깃줄 최대 개수 100...위치의 번호는 500이하...
    # 2**100
    # -> X

# => 그리디(?)
    # 가장 많이 교차하는 것 부터..?
    # 그럼 특정 전깃줄이 교차시키는 다른 전깃줄 개수 부터 파악해야하고
    # 그것을 제거 했을 때, 다시 다 갱신해야함


# => 결국 교차하지 않으려면,이전 줄 보다 B가 더 커야함
    # 최장 증가 부분 수열 알고리즘
        #=> DP