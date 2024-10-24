import sys
from collections import Counter

sys.stdin = open("input.txt", 'r')

n, m = list(map(int, sys.stdin.readline().split()))

names_cnt = Counter(list(sys.stdin.readlines()))

no_listen_see = []
for (name,cnt) in names_cnt.items():
    if cnt == 2:
        no_listen_see.append(name.strip())

print(len(no_listen_see))
no_listen_see.sort()

for name in no_listen_see:
    print(name)