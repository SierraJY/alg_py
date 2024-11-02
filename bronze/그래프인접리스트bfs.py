# 인접 리스트로 구현
# 서버 컴퓨터와 연결되지 않은 컴퓨터는 수학교실의 컴퓨터로 간주한다
# 수학교실의 컴퓨터 개수는 몇 개인가?

from collections import deque

def solution(n, edges):
    adj_list = [[] for _ in range(n+1)]

    for v_a, v_b in edges:
        adj_list[v_a].append(v_b)
        adj_list[v_b].append(v_a)

    visited_list = [0 for _ in range(n + 1)] # 1에서만 도달 가능성 판단하면 되니까 정점마다 초기화 할 필요X
    def bfs(com) :

        queue = deque()
        queue.append(com)

        while queue :
            now_que_cnt = len(queue)
            for _ in range(now_que_cnt):
                v = queue.popleft()
                for linked_com in adj_list[v]:
                    if visited_list[linked_com] == 0 :
                        visited_list[linked_com] = 1
                        queue.append(linked_com)

    bfs(1)

    return n - visited_list[1:].count(1)




print(solution(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))
print(solution(12, [[1, 2], [1, 7], [1, 8], [1, 6], [8, 11], [11, 12]]))
print(solution(14, [[1, 6], [1, 5], [6, 7], [7, 8], [9, 8], [3, 4], [4, 14]]))
print(solution(15, [[1, 4], [1, 5], [9, 5], [9, 6], [7, 9], [7, 14]]))

# how
# visited 리스트를 이용해서 '1에서 출발해서' 방문하지 못했던 Vertex만 찾으면됨
# 방문 방식에서는 BFS를 사용

# 주의할 것
# DFS로도 풀 수 있음, 인접리스트, 인접행렬과 DFS, BFS는 상관없음
# 그래프 표현 방식과 그래프 탐색 알고리즘은 서로 독립적

# 알게된 것
# 인접리스트도 0 인덱스는 편의상 비워는것이 좋음
