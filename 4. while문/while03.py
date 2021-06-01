import sys
x = int(sys.stdin.readline())
p = x
cycle = 0

while True:
    cycle += 1
    y = x // 10 + x % 10
    x = str(x)[-1] + str(y)[-1]
    x = int(x)
    if int(x) == p:
        break
print(cycle)    