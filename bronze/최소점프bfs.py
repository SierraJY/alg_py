# 현수는 놀이터에서 놀다가 집으로 가려고 합니다
# 놀이터의 위치와 집의 위치가 수직선상의 좌표 점으로 주어집니다
# 놀이터는 수직선상의 0지점입니다
# 현수는 놀이터에서 스카이콩콩을 타고 점프를 하면서 집으로 이동하려고 합니다.
# 점프는 다음과 같은 규칙으로 합니다.
# 1) 현재 지점에서 앞으로 1만큼 점프이동할 수 있습니다
# 2) 현재 지점에서 뒤쪽으로 1만큼 점프이동할 수 있습니다
# 3) 현재 지점에서 앞쪽으로 5만큼 긴 점프이동을 할 수있습니다
# 매개변수 home에 현수의 집의 위치가 주어지면 놀이터에서 집까지 최소 몇 번의 점프로 집에
# 도착할 수 있는지 최소 점프횟수를 구하여 반환하세요

from collections import deque

def bfs(home):

    visited = [0] * int(1e4) # 방문 기록이 있었던 지점인지 확인하기 위힌 리스트
    now_jump_level = 0  # 점프 횟수

    queue = deque()
    queue.append(0)
    visited[0] = 1

    while queue:
        now_situations = len(queue) # 현재까지 진행한 상황 개수

        for _ in range(now_situations) :

            v = queue.popleft()
            if v == home : return now_jump_level

            for vc in [v-1, v+1, v+5]:
                if vc >=0 and vc<=1e4 and visited[vc]==0:
                    visited[vc] = 1
                    queue.append(vc)

        now_jump_level += 1
def solution(home):

    return bfs(home)

print(solution(10))
print(solution(14))
print(solution(25))
print(solution(24))
print(solution(345))

# 주의할 점
# 각 점프마다 가능한 세 가지 이동(+1, -1, +5)을 모두 큐에 넣으면 오래거림

# 알게된 것
# 최소(거리)와 관련된 문제이면 BFS를 고려