from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    on_bridge_weight = 0

    wait_trucks = deque(truck_weights)
    on_bridge = deque()

    while on_bridge or wait_trucks:
        time += 1

        if on_bridge:
            # 길이 업데이트
            for i in range(len(on_bridge)):
                on_bridge[i][1] -= 1
            # on_bridge에서 제거
            if on_bridge[0][1] == 0:
                poped_truck = on_bridge.popleft()
                on_bridge_weight -= poped_truck[0]

        if wait_trucks and on_bridge_weight + wait_trucks[0] <= weight and len(on_bridge) < bridge_length:
            start_truck = wait_trucks.popleft()
            on_bridge_weight += start_truck
            on_bridge.append([start_truck, bridge_length])

    return time

print(solution(2,10,[7,4,5,6]))

# what
# 최단 시간 안에 다리를 건널 때, 걸리는 시간

# how
# 대기 트럭 및 다리를 건너는 트럭에 대하여 Queue 2개 사용
# 다리 위에 올라간 트럭은 현재 다리위의 위치와 함께 [,]로 Queue에 저장
# 남은 트럭이 있고, 트럭 하나를 올렸을 때 총 무게가 weight이하이고, 트럭 하나를 올렸을 때 트럭 수가 bridge_length 이하일 때만 트럭을 다리로
