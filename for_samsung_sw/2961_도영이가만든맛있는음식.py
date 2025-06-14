# note : 이진법 계산 활용, 모든 경우의 수(즉, 모두 포함하는 경우를 표시하는 비트마스킹)를 의미하는 정수를 만드는 법
# note : bin 내장함수

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
foods = [tuple(map(int, input().split())) for _ in range(N)]
min_diff = int(1e9)+1

bits = 0 #모든 경우의 수를 십진수로 저장한 변수
for i in range(N):
    bits += 2**i

for bit in range(1, bits + 1):
    # print("------",bin(bit))
    s = 1
    b = 0

    for i in range(N):
        if bit & (1 << i):
            s *= foods[i][0]
            b += foods[i][1]

    min_diff = min(min_diff, abs(s-b))

print(min_diff)