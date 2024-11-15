def solution(tickets):
    TICKET_CNT = len(tickets)  # 전체 티켓 수
    used_ticket = [0 for _ in range(TICKET_CNT)]  # 각 티켓의 사용 여부를 추적하는 리스트

    def dfs(arrive, course):
        """
        현재 공항에서 시작하여 모든 티켓을 사용하는 경로를 찾는 재귀 함수

        Args:
            arrive (str): 현재 도착한 공항
            course (List[str]): 현재까지의 여행 경로
        Returns:
            List[str] or False: 유효한 경로를 찾으면 경로 리스트, 아니면 False
        """

        # 모든 티켓을 사용했는지 확인 (티켓 개수 + 1 = 방문한 공항 수)
        if len(course) == TICKET_CNT + 1:
            return course

        # 현재 공항에서 출발하는 사용 가능한 티켓의 인덱스를 저장할 리스트
        can_use_now_ticket = []

        # 현재 공항(arrive)에서 출발하는 미사용 티켓 찾기
        for t in range(TICKET_CNT):
            if arrive == tickets[t][0] and used_ticket[t] == 0:
                can_use_now_ticket.append(t)

        # 사용 가능한 티켓이 없으면 False 반환 (더 이상 진행 불가)
        if len(can_use_now_ticket) == 0:
            return False

        # 도착 공항을 기준으로 알파벳 순으로 정렬 (사전순 처리)
        can_use_now_ticket.sort(key=lambda t: tickets[t][1])

        # 가능한 모든 다음 경로에 대해 DFS 수행
        for go_next in can_use_now_ticket:
            used_ticket[go_next] = 1  # 현재 티켓 사용 표시

            # 다음 공항으로 이동하여 DFS 재귀 호출
            # tickets[go_next][1]: 다음 도착지
            # course + [tickets[go_next][1]]: 현재 경로에 다음 도착지 추가
            result = dfs(tickets[go_next][1], course + [tickets[go_next][1]])

            if result:  # 유효한 경로를 찾은 경우
                return result

            # 유효한 경로를 찾지 못한 경우, 티켓 사용 취소 (백트래킹)
            used_ticket[go_next] = 0

        return False  # 모든 가능한 경로를 시도했지만 실패

    # "ICN"에서 시작하여 DFS 수행
    return dfs("ICN", ["ICN"])

# What
# "ICN"에서 출발하여 주어진 항공권을 모두 이용하여 여행할 수 있는 경로를 찾는 문제
# 모든 항공권을 사용해야 함

# How
# DFS 선택 이유
#  - 모든 티켓을 사용하는 경로를 찾아야 하므로 끝까지 탐색이 필요
#  - 한 경로를 끝까지 탐색 후 실패하면 다른 경로를 시도해야 하므로 DFS가 적합
#  - BFS도 가능하나 경로 저장과 관리가 더 복잡해질 수 있음
# 
# 구현 전략
#  - used_ticket 배열로 티켓 사용 여부 관리 (중복 사용 방지)
#  - 현재 위치에서 출발하는 미사용 티켓들을 찾아 알파벳 순으로 정렬
#  - 경로를 찾을 때까지 재귀적으로 DFS 수행
#  - 실패 시 백트래킹하여 다른 경로 탐색
#
# 종료 조건
#   모든 티켓을 사용한 경우 (경로 길이 = 티켓 수 + 1)
#   또는 현재 공항에서 사용할 수 있는 티켓이 없는 경우

# 주의할 것
# 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return

# 알게된 것
# 최단 경로를 찾는 것이 아니라 모든 티켓을 사용하는 유효한 경로를 찾는 것이 목적이라면 DFS가 더 적합
# BFS는 매우 복잡
# 문제에 주어진 조건은 그냥 주어진 것이 아님, 반드시 이용해야함