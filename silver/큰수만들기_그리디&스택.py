def solution(number, k):
    number = [int(n) for n in number]
    stack = []

    for n in number:
        while stack and k > 0 and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)

    return "".join([str(n) for n in stack[:len(stack)-k]])


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("987654321", 5)) #stack[:len(stack)-k]에 대한 이유

# what
# number에서의 숫자 k 개만 제거했을 떄 얻을 수 있는 가장 큰 숫자 (numbser에서의 순서를 바꿀 수는 없음)

# how
# 스택 & 그리디
# 스택 : 선택할 숫자들 저장
# 그리디 : 항상 현재 자리에 넣을 수 있는 수는 가능한 숫자들 중 가장 큰 걸 선택하되 제거 가능한 개수가 남아있을 때만

# 주의할것
# O(n)에 해결 못하면 시간초과