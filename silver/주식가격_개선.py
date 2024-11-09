def solution(prices):
    LEN = len(prices)

    sec_list = [i for i in range(LEN - 1, -1, -1)]
    stack = []

    for i in range(0, LEN):
        while stack and prices[stack[-1]] > prices[i]:
            poped = stack.pop()
            sec_list[poped] = i - poped

        stack.append(i)

    return sec_list

# how
# 스택에 가격의 prices에서의 인덱스를 삽입함
# 스택에서 해당 가격이 빠졌을 때와 for문의 i와 시간 차이를 sec_list에 추가