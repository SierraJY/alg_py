import sys

sys.stdin = open(0, 'r')

num = int(sys.stdin.readline())
sticks = list(map(int, sys.stdin.readlines()))

hiding_stick_idx = len(sticks) - 1
can_see = 1

for i in range(len(sticks)-1, -1, -1):
    if sticks[i] > sticks[hiding_stick_idx]:
        can_see += 1
        hiding_stick_idx = i

print(can_see)
