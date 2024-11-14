def solution(n, computers):
    all_network = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if computers[i][j] == 1:
                all_network[i].append(j)

    def dfs(com):
        visited[com] = 1
        for next_com in all_network[com]:
            if visited[next_com] == 0:
                dfs(next_com)

    visited = [0 for _ in range(n)]
    net_cnt = 0
    for visited_idx in range(n):
        if visited[visited_idx] == 1: continue

        net_cnt += 1
        dfs(visited_idx)

    return net_cnt

# what
# 네트워크의 개수

# how
# 네트워크 구현 : 그래프(인접리스트)
# dfs 사용 : 최소거리를 구하는 것이 아니니까
# visited 사용하여, 1번부터 쭉 가보고, visited에 0인 다음 노드 부터 또 쭉 가보기

# 주의할 것
# 이 문제에서는 컴퓨터 번호가 0부터 사용되므로 그냥 인덱스 0부터 사용함
# 하나의 네트워크 내의 컴퓨터 개수 등은 필요없음