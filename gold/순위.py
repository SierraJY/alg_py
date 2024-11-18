def solution(n, results):
    graph = [[] for _ in range(n + 1)]

    for a, b in results:
        graph[a].append((b, 1))  # a가 b한테 이김 :  1
        graph[b].append((a, -1))  # b가 a한테 짐 : -1

    for a in range(1, n + 1):
        for b in graph[a]:
            if b[1] == 1: # a가 b를 이겼다면 b가 이긴 상대들은 a도 이길 수 있음
                for to_lose_b in graph[b[0]]:
                    if to_lose_b[1] == 1 and to_lose_b not in graph[a]:
                        graph[a].append(to_lose_b)

            elif b[1] == -1: # a가 b한테 졌다면 b가 진 상대들은 a도 짐
                for to_win_b in graph[b[0]]:
                    if to_win_b[1] == -1 and to_win_b not in graph[a]:
                        graph[a].append(to_win_b)

    cnt = 0
    for a in range(1, n + 1):
        if len(graph[a]) == n - 1: cnt += 1

    return cnt

# what
# 몇몇 경기의 결과 분실, 정확하게 순위를 매길 수 있는 선수의 수 찾기

# how
# 가중치 무방향 그래프 사용 (가중치는 승패 표시용)
# A선수가 B선수한테 승리했다면, B선수한테 패배한 목록을 A선수 전적으로 가져옴 (O)
# A선수가 B선수한테 패배했다면, B선수한테 승리한 목록을 A선수 전적으로 가져옴 (O)

# 주의할 것
# A가 B를 이겼다면 A를 이긴 C를 B가 이길 수는 없음(?)

# 생각했었던 how들
# 가지고 있는 간선의 개수 사용(X)
# 승패를 가중치로 가중치 무방향 그래프 사용(X)
# A선수에서 출발에서 B선수까지 도달 가능하면 순위를 매길 수 있으니까, 각 선수마다 도달 가능한 선수 수를 이용(X)

