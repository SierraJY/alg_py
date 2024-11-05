from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)

    heaviest_idx = len(people) - 1

    boat_cnt = 0
    while people:
        if 0 == heaviest_idx : pass
        elif people[0] + people[heaviest_idx] > limit : pass
        elif people[0] + people[heaviest_idx] <= limit:
            people.popleft()
            heaviest_idx -= 1

        people.pop()
        heaviest_idx -= 1
        boat_cnt += 1

    return boat_cnt

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([50, 50, 50, 50], 100))

# how
# 그리디 & 투 포인터
# 정렬 부터 수행 : O(NlogN)
# 혼자인 남은 경우 혼자 태우면 됨
# 가장 무거운 사람과 가장 가벼운 사람이 limit 초과면 무거운 사람은 반드시 혼자 타야하므로 보트 바로 태움 pop
# 가장 무거운 사람과 가장 가벼운 사람이 limit 이내면 둘을 같이 태우는게 최선의 선택이므로 같이 태운다음 pop, popleft
# 주의할 점
# 한번에 두 명 태울 수 있을 때 right 인덱스 처리 생각 해보기