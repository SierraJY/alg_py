import sys

sys.stdin = open("input.txt", 'r')

N = int(sys.stdin.readline())

for age, name in sorted([[int(m[0]), m[1]]for m in [m.split() for m in sys.stdin.readlines()]], key = lambda m : m[0]):
    print(age, name)