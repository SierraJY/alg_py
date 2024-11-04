# 프로그래머스 : 체육복
def solution(n, lost, reserve):
    new_lost = sorted([l for l in lost if l not in reserve])
    new_reserve = set([r for r in reserve if r not in lost])

    cant_borrow = len(new_lost)
    for l in new_lost:
        if (l - 1) in new_reserve:
            cant_borrow -= 1
            new_reserve.remove(l - 1)
        elif (l + 1) in new_reserve:
            cant_borrow -= 1
            new_reserve.remove(l + 1)

    return n - cant_borrow

# what
# 여벌의 체육복을 빌려주었을때, 수업을 들을 수 있는 학생의 최댓값

# how
# 우선 여분이 있는 분실자는 lost와 reserve에서 제거
# 중요) 분실자 명단 정렬
# 여분이 없는 분실자 l에 대해 l-1 or l+1이 reserve에 있으면 빌리지 못한 사람수 - 1 하고 빌린 사람 번호 reserve에서 pop
# 인원수 - 빌리지 못한 사람수

# 주의할 것
# 반례
# lost = [4, 2], reserve = [3, 5]인 경우:
# 4번 학생을 먼저 처리하면 3번 학생의 여벌 체육복을 사용
# 2번 학생은 남은 5번 학생의 체육복을 빌릴 수 없음
# 결과적으로 3명만 체육복을 가지게 됨

# 알게된 것
# 그리디 알고리즘의 관점에서 '지역 최적해'를 선택할 때 입력 배열이 정렬되어 있지 않으면 전체 최적해를 보장할 수 없는 대표적인 사례

# 알아야할 파이썬
# .pop(.index()) 대신 중복되는 요소가 없으면 Set.remove()가 나을 수 있다