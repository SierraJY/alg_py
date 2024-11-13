def solution(n, wires):
    tree = [[] for i in range(n + 1)]
    for v1, v2 in wires:
        tree[v1].append(v2)
        tree[v2].append(v1)

    def dfs(next_v, cutted):
        visited[next_v] = 1
        cnt = 1
        for v in tree[next_v]:
            if visited[v] == 0 and v != cutted:
                cnt += dfs(v, cutted)
        return cnt

    min_diff = 1e9
    for v1, v2 in wires:
        visited = [0] * (n + 1)
        left_cnt = dfs(v1, v2)
        right_cnt = dfs(v2, v1)
        min_diff = min(min_diff, abs(left_cnt - right_cnt))

    return min_diff

# what
# 전력망을 끊이 2개의 전력망이 최대한 비슷한 개수의 송전탑을 가지도록 할 때, 절대값 차이

# how
# 입력으로 트리가 들어온다고 했음 (따라서, 싸이클 없음)
# 그렇기 때문에 어떤 wire를 끊든 2등분이 됨
# 트리 구현 : 인접리스트

# n은 100이하이므로 최대 간선 개수 99개
# 충분히 BF가능
# 끊어진 와이어를 기준으로 두 전력망의 송전탑 개수 체크

# 알게된 것
# 입력으로 트리가 들어온다고 했음 (따라서, 싸이클 없음)
# 그렇기 때문에 어떤 wire를 끊든 2등분이 됨

