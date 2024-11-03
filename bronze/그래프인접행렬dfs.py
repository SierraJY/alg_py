# 인접행렬 구현
# 서버 컴퓨터(1번)와 연결되지 않은 컴퓨터는 수학교실의 컴퓨터로 간주한다
# 수학교실의 컴퓨터 개수는 몇 개인가?

def solution(n, edges):

    visited = [0] * (n + 1)  # 0번 편의상 사용 X
    adj_matrix= [[0] * (n+1) for _ in range(n+1)]

    for a_v, b_v in edges:
        adj_matrix[a_v][b_v] = 1
        adj_matrix[b_v][a_v] = 1

    def dfs(com):
        for link_test_com in range(1, n + 1):
            if visited[link_test_com] == 0 and adj_matrix[com][link_test_com] == 1:
                visited[link_test_com] = 1
                dfs(link_test_com)

    dfs(1)

    return n - visited[1:].count(1)

print(solution(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))
print(solution(12, [[1, 2], [1, 7], [1, 8], [1, 6], [8, 11], [11, 12]]))
print(solution(14, [[1, 6], [1, 5], [6, 7], [7, 8], [9, 8], [3, 4], [4, 14]]))
print(solution(15, [[1, 4], [1, 5], [9, 5], [9, 6], [7, 9], [7, 14]]))

# how
# visited 리스트를 이용해서 '1번에서 출발해서' 방문하지 못했던 Vertex만 찾으면됨
# 방문 방식에서는 DFS를 사용

# 주의할 것
# 파이썬 이차원 리스트 초기화는 리스트 컴프리헨션으로

# 알게된 것
# 1 : 재귀함수는 종료조건이 명확하거나 아니면 재귀 시작 조건 자체가 명확해도된다
# 2 : DFS에서도 visited 배열을 만들 수 있다!, visited 배열과 dfs, bfs는 상관없다
# 그냥 재방문을 예방하는 용도이다
