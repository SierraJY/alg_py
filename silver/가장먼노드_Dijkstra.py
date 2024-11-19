import heapq

def solution(n, edge):
    INF = 1e9  # 무한대 값 설정

    # 그래프 초기화: 인접 리스트 사용
    graph = [[] for _ in range(n + 1)]
    d = [INF for _ in range(n + 1)]  # 최단 거리 테이블 초기화

    # 양방향 간선 정보 저장
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)

    start_v = 1  # 시작 노드 (1번 노드)
    d[start_v] = 0  # 시작 노드까지의 거리는 0
    pq = [(0, start_v)]  # 우선순위 큐 초기화: (거리, 노드)

    # Dijkstra 알고리즘 시작
    while pq:
        distance, a = heapq.heappop(pq)

        # 이미 처리된 노드라면 무시
        if d[a] < distance:
            continue

        # 현재 노드와 연결된 다른 노드들 확인
        for b in graph[a]:
            if distance + 1 < d[b]:  # 현재 노드를 거쳐 가는 것이 더 짧은 경우
                d[b] = distance + 1
                heapq.heappush(pq, (d[b], b))

    # 가장 멀리 떨어진 노드의 개수 반환
    return d.count(max(d[1:]))

# what
# 1번 노드에서 가장 멀리 떨어진 노드가 몇 개인지를 return

# how
# 특정 노드에서 최단 거리가 가장 큰 노드'들'을 찾는 문제이므로 Dijkstra 알고리즘으로 볼 수 있음

# 주의할 것
# 모든 간선의 가중치 1인 문제