def solution(name):
    # 문자 변환 조작 횟수 계산
    trans_cnt = 0
    for c in name:
        trans_cnt += min(ord(c) - ord('A'), ord('A') + (ord('Z')-ord('A')+1) - ord(c))

    # 현재 위치 커서 이동 조작 횟수 계산
    move_cnt = len(name) - 1
    for i in range(len(name)):

        # 현재 위치부터 연속된 A 찾기
        c_A_l_p = i + 1 # continuos_A_last_pos : c_A_l_p
        while c_A_l_p < len(name) and name[c_A_l_p] == 'A':
            c_A_l_p += 1
            m = c_A_l_p
        move_cnt = min([move_cnt, 2*i + len(name)-c_A_l_p, i + 2 * (len(name)-c_A_l_p)])

    return trans_cnt + move_cnt

print(solution("JEROEN"))
print(solution("BCAABCDAAAAAAD"))

# what
# 조이스틱의 최소 조작 횟수

# how
# 시뮬레이션 + 완전 탐색
# 문자 전환 조작 & 현재 위치 커서 이동 조작 나누어서 조작
# 문자 전환 조작
# 알파벳 순서를 이용해서 위 or 아래 중 어디가 덜 조작하는지 계산
# ⭐️ 커서 이동 조작
# 현재 위치의 다음 위치 부터, 길이가 1이상 연속된 'A'가 있을때 연속된 'A'의 마지막 위치를 파악한다
# 현재 위치 까지의 가장 적게 이동했던 횟수와 (초기값 : 이름 길이 - 1)
# 현재 위치 까지 왔다가 연속된 'A'를 마주치지 않고 왼쪽 방향으로 돌아가서 바꿔야할 문자들에 도달하는 방식의 이동 횟수
# 현재 위치에서 'A'를 마주치기 전까지 왼쪽 방향으로 연속된 바꿔야할 문자들을 바꾸고 다시 오른방향으로 원위치로 돌아와서 바꿔야할 문자들에 도달하는 방식
# 의 이동횟수를 비교

# 주의할 것
# BF 방식 : 너무 오래 걸림
# 이 문제가 그리디가 맞긴 한 이유 : 문자 전환 조작 자체는 그리디가 맞긴함

# 알게된 것
# 순환가능한 배열에서
# 더 오른쪽에 있는 요소 인덱스와 더 왼쪽에 있는 요소 인덱스를 알아낸 후
# (오른쪽 인덱스 - 왼쪽 인덱스)
# (왼쪽 인덱스 + 배열길이 - 오른쪽 인덱스)
# 위의 두 값 중 작은 값이 최단 거리가 된다

# ABCDEFGHIJKLMOPQRSTUVWXYZ
# 알파벳 개수 : 26
# ord('Z') - ord('A') + 1 = 26