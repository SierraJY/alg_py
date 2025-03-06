import sys
from collections import defaultdict

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    wish_s = list(map(int, input().split()))

    visited = [0 for _ in range(n + 1)]
    team_cnt = 0

    for i in range(n):
        if i+1 == wish_s[i]:
            visited[i+1] = 1
            team_cnt += 1

    for i in range(1, n + 1):
        if visited[i]:
            continue

        cur_node = i
        back_cnt = 1
        dfs_check = defaultdict(int)
        while visited[cur_node] == 0:
            visited[cur_node] = 1
            dfs_check[cur_node] = back_cnt
            back_cnt += 1
            cur_node = wish_s[cur_node-1]

        if cur_node in dfs_check:
            team_cnt += back_cnt - dfs_check[cur_node]

    print(n - team_cnt)

# 아이디어 & 알고리즘
# 자기 자신을 선택하면 한팀 + 1
# 싸이클이 있으면 한팀 + 1
# => 싸이클 어떻게 탐지? 한 방향 그래프
# => 위상정렬?X 위상정렬로는 존재 유무만 판단 가능
# => DFS, 사이클 체크 배열에 자기 전에 몇 개 있었는지 저장?

# 주의할 것
# 재귀로 하면 시간 초과 or 재귀 리미트 도달
# 재귀 대신 반복문 사용

