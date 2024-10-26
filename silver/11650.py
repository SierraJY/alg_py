import sys

sys.stdin = open("input.txt", 'r')

N = int(sys.stdin.readline())

coordinate = [tuple(map(int, c.strip().split())) for c in sys.stdin.readlines()]

coordinate.sort(key = lambda r : (r[0], r[1]))

for x, y in coordinate:
    print(x, y)

