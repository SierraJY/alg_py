# <정답 코드>
import sys

sys.stdin = open(0, 'r')
input = sys.stdin.readline

def check_pal(word, l, r):
    while l < r:
        if word[l] != word[r]:
            return False
        l += 1
        r -= 1
    return True

T = int(input())

for _ in range(T):
    word = input().strip()

    l = 0
    r = len(word) - 1

    is_pal = True
    while l < r:
        if word[l] != word[r]:
            is_pal = False
            break
        l += 1
        r -= 1

    is_similar_pal = False
    if check_pal(word, l + 1, r) or check_pal(word, l, r - 1):
        is_similar_pal = True

    if is_pal:
        print(0)
    elif is_similar_pal:
        print(1)
    else:
        print(2)

# 아이디어 & 알고리즘
# 회문 판별 어떻게 ?
# =>  스택? X
# 스택은 짝만 찾을 수고 회문을 찾는데는 X

# => 슬라이딩 윈도우(투포인터)?

# 유사 회문 판별 어떻게?

# <틀린 코드>
# 안되는 이유 :
# 이때 왼쪽 문자만 삭제하거나 오른쪽 문자만 삭제하는 두 가지 경우 중 한 가지 경우만 선택하고 나머지 경우는 무시
# 이로 인해 두 가지 선택지 모두 가능한 상황에서 한 가지 선택지만 검사하고 다른 선택지를 놓치는 경우가 발생
# 반례 : abcddcdba

# import sys
#
# sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
#
# T = int(input())
#
# for _ in range(T):
#     word = input().strip()
#     l = 0
#     r = len(word) -1
#
#     chance = True
#     no_pal = False
#
#     while l <= r:
#         if word[l] != word[r]:
#             if chance:
#                 if word[l+1] == word[r]:
#                     l += 1
#                     chance = False
#                 elif word[l] == word[r-1]:
#                     r -= 1
#                     chance = False
#                 else:
#                     no_pal = True
#                     break
#             else:
#                 no_pal = True
#                 break
#         l += 1
#         r -= 1
#
#     if no_pal:
#         print(2)
#     elif chance:
#         print(0)
#     else:
#         print(1)



