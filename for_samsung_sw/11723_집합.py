# note : set()에는 add와 remove 메서드가 있다
# note : set()에 in 연산자 사용가능

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

M = int(input())
S = set()
for _ in range(M):
    order = input().split()

    if order[0] == 'add':
        S.add(int(order[1]))
    elif order[0] == 'remove':
        if int(order[1]) in S: S.remove(int(order[1]))
    elif order[0] == 'check':
        if int(order[1]) in S: print(1)
        else: print(0)
    elif order[0] == 'toggle':
        if int(order[1]) in S: S.remove(int(order[1]))
        else : S.add(int(order[1]))
    elif order[0] == 'all':
        S = set([i for i in range(21)])
    elif order[0] == 'empty':
        S = set()