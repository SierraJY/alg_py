import sys
from collections import Counter

sys.stdin = open("input.txt", 'r')

n = int(sys.stdin.readline())
names = [s.strip() for s in sys.stdin.readlines()]
names_cnt = Counter(names)

for name, cnt in names_cnt.items():
    if cnt % 2 != 0:
        print(name)
        break