import sys

sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    cand = []

    for _ in range(N):
        cand.append(tuple(map(int, sys.stdin.readline().split())))

    cand.sort()

    eliminated = 0
    current_best = 0
    for i in range(1,N):
        if cand[current_best][1] < cand[i][1]:
            eliminated += 1
        else:current_best=i

    print(N - eliminated)

# what
# 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발
# 최대로 선발할 수 있는 최대 신입사원의 수
# 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해
# 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.

# How
# 시도1
# A와 B를 1대1일로 비교해보는 방법말고 다른 방법이 있나? => 시간초과

# 시도2(시간 복잡도를 O(N²)에서 O(NlogN)으로 개선)
# 일단 서류 점수로 정렬
# 서류 일등을 기준으로 면접 순위도 낮으면 바로 탈락
# 서류 일등 보다 면접 순위는 높으면 다음 기준은 그 지원자로 설정
# 새로운 기준 지원자보다 면접 순위가 낮으면 어차피 서류 일등도 못이기기 때문
# 즉, 한 성적을 기준으로 정렬하면, 다른 성적만 비교하면 됨

# 주의할 점
# 성적이 아니라 순위가 주어짐(동석 차는 없음)