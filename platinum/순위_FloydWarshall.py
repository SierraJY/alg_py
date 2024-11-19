def solution(n, results):
    # 경기 결과를 모르는 경우를 표현하기 위한 큰 값
    UNKNOWN = int(1e9)

    # graph[i][j] = 1: i가 j를 이김
    # graph[i][j] = -1: i가 j에게 짐
    # graph[i][j] = UNKNOWN: 승패를 알 수 없음
    graph = [[UNKNOWN for _ in range(n + 1)] for _ in range(n + 1)]

    # 자기 자신과의 경기는 없으므로 0으로 초기화
    for i in range(1, n + 1):
        graph[i][i] = 0

    # 주어진 경기 결과로 그래프 초기화
    for win, lose in results:
        graph[win][lose] = 1  # 승리
        graph[lose][win] = -1  # 패배

    # 플로이드-워셜 알고리즘을 통한 순위 관계 추론
    for mid in range(1, n + 1):
        for v1 in range(1, n + 1):
            for v2 in range(1, n + 1):
                # A가 B를 이기고, B가 C를 이겼다면 A는 C를 이김
                if graph[v1][mid] == 1 and graph[mid][v2] == 1:
                    graph[v1][v2] = 1
                    graph[v2][v1] = -1
                # A가 B에게 지고, B가 C에게 졌다면 A는 C에게 짐
                elif graph[v1][mid] == -1 and graph[mid][v2] == -1:
                    graph[v1][v2] = -1
                    graph[v2][v1] = 1

    # 모든 선수와의 승패 관계가 결정된 선수 수 계산
    answer = 0
    for i in range(1, n + 1):
        print(graph[i][1:])
        if UNKNOWN not in graph[i][1:]:
            answer += 1

    return answer

# what
# 몇몇 경기의 결과 분실, 정확하게 순위를 매길 수 있는 선수의 수 찾기

# how
# 플로이드-와샬을 변형
# mid를 통해 경기 결과를 전파(?)

# 주의할 것
# 해당 문제의 가정
#    - A가 B를 이기고, B가 C를 이겼다면 반드시 A는 C를 이김
#    - A가 B를 이겼다면, B를 이긴 선수는 반드시 A를 이김
#    - A가 B를 이겼다면, A에게 진 선수는 반드시 B에게도 짐