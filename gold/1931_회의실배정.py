import sys

sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline()) # 회의 개수

seminar = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    seminar.append((start, end))

seminar.sort(key = lambda x : (x[1], x[0]))

seminar_cnt = 0
now_time = 0

for s_t, e_t in seminar:

    if s_t < now_time : continue

    seminar_cnt += 1
    now_time = e_t

print(seminar_cnt)


# what
# 한 개의 회의실에 대한 회의 배정
# 배정 가능한 최대 회의 개수

# how
# 그리디
# - 시도 1 (X)
# 같은 시작시간에 대해서는 무조건 짧은 회의 먼저 넣기
# 시작 시간 기준으로 해시테이블 만들기
# - 시도 2 (X)
# 우선순위 큐 사용
# 현재 시간에 대하여 넣을 수 있는 회의 하나 Pop
# 다음 루트 노트에 회의가 더 짧으면 버리고 짧은 거 Pop

# 주의할 점
# 끝나는 시간은 반드시 시작 시간보다 같거나 이후임
# 따라 끝나는 시간만 잘 고려하면됨

# 알게된 것
# 문제의 본질을 잘못파악함
# 디스크 컨트롤러와 같은 문제로 생각함
# 디스크 컨트롤러 문제는 그리디가 아님