from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    on_bridge_weight = 0

    wait_trucks = deque(truck_weights)
    on_bridge = deque([0] * bridge_length)

    while on_bridge:
        time += 1
        # on_bridge에서 제거
        poped_truck = on_bridge.popleft()
        on_bridge_weight -= poped_truck

        if wait_trucks:
            if (on_bridge_weight + wait_trucks[0]) <= weight:
                start_truck = wait_trucks.popleft()
                on_bridge_weight += start_truck
                on_bridge.append(start_truck)
            else:
                on_bridge.append(0)

    return time

print(solution(2,10,[7,4,5,6]))

# what
# 최단 시간 안에 다리를 건널 때, 걸리는 시간

# how
# 대기 트럭 및 다리를 건너는 트럭에 대하여 Queue 2개 사용
# 다리 위의 트럭이 없는 위치를 [0]으로 관리

# 주의할 것
# 조건문 구성 : if문 두개를 and로 합치면 안됨 -> 무한루프
