def solution(prices):
    sec_list = [0] * len(prices)
    stack = []

    for order, pr in enumerate(prices):

        for i in range(len(stack)):
            stack[i][2] += 1

        while stack and stack[-1][1] > pr:
            poped = stack.pop()
            sec_list[poped[0]] = poped[2]

        stack.append([order, pr, 0])

    while stack:
        poped = stack.pop()
        sec_list[poped[0]] = poped[2]

    return sec_list

# what
# 가격이 떨어지지 않은 기간은 몇 초인지 return

# how
# 스택 사용 : 스택에 넣을 때 순서와 스택에서 기다리는 시간 함께 저장
# 시간 기록용 배열 따로 사용

# 각 초마다, 우선 스택에 있는 원소들의 스택에서 대기하는 시간 +1
# 스택에서 pop되면 같이 저장된 순서를 인덱스로 시간 기록용 배열에 시간 저장
# 더이상 prices가 없고 스택에 남아있는게 있으면 while문으로 처리