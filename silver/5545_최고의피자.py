import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline()) # 토핑 종류
A, B = map(int, sys.stdin.readline().split()) # 도우 가격, 토핑의 가격
C = int(sys.stdin.readline()) # 도우의 열량
D = [int(sys.stdin.readline()) for _ in range(N)]
D.sort(reverse=True)

k = 0 # 현재 선택된 토핑 수
cal = C #현재 칼로리

for i in range(N):
    new_cal = cal + D[i]
    if new_cal/(A+B*(k+1)) >= cal/(A+B*k):
        k += 1
        cal = new_cal

print(cal//(A+B*k))



# what
# 1원당 열량이 가장 높은 피자인 최고의 피자의 열량을 구하시오

# how
# 그리디
# 우선 토핑을 열량 순으로 정렬 해두어야함(가격은 모두 동일하니까, 앞에 있을 수록 1원당 열량이 높음)
# 1원당 열량이 높아지면 선택
