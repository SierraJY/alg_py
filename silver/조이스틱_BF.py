from itertools import permutations

def solution(name):
    # 문자 변환 조작 횟수 계산
    trans_cnt = 0
    for c in name:
        trans_cnt += min(ord(c) - ord('A'), ord('A') + (ord('Z')-ord('A')+1) - ord(c))

    # 현재 위치 커서 이동 조작 횟수 계산
    move_cnt = 1e9
    to_trans_point = [i for i in range(1, len(name)) if name[i] != 'A']
    availables = permutations(to_trans_point)
    for ava in availables:
        now_cursor = 0
        tmp_move_cnt = 0

        for next_point in ava:
            right, left = max(now_cursor, next_point), min(now_cursor, next_point)
            right_diff = right - left
            left_diff = left + len(name) - right

            now_cursor = next_point
            tmp_move_cnt += min(right_diff, left_diff)

        move_cnt = min(move_cnt, tmp_move_cnt)

    return trans_cnt + move_cnt

print(solution("JAZ"))

# what
# 조이스틱의 최소 조작 횟수

# how
# 시뮬레이션 + 완전 탐색
# 문자 전환 조작 & 현재 위치 커서 이동 조작 나누어서 조작
# 문자 전환 조작은 알파벳 순서를 이용해서 위 or 아래 중 어디가 덜 조작하는지 계산
# 커서 이동은 변환해야하는 위치를 완전탐색해서 가장 적게 이동하는 루트 찾고 얼마나 조작하는지 계산

# 주의할 것
# 원래 하려했던 그리디 방식 : 전역 최적해가 아님
# 시뮬레이션 + 그리디
# 현재 커서 위치의 알파벳 index만큼 조작 +cnt
# 커서 위치에서 +-1 씩 탐색하고 옮기기
# 반복
# buf == name이 되었을 때 종료

# 알게된 것
# 순환가능한 배열에서
# 더 오른쪽에 있는 요소 인덱스와 더 왼쪽에 있는 요소 인덱스를 알아낸 후
# (오른쪽 인덱스 - 왼쪽 인덱스)
# (왼쪽 인덱스 + 배열길이 - 오른쪽 인덱스)
# 위의 두 값 중 작은 값이 최단 거리가 된다

# ABCDEFGHIJKLMOPQRSTUVWXYZ
# 알파벳 개수 : 26
# ord('Z') - ord('A') + 1 = 26

# 알아야할 파이썬
# ord()
# permutations()