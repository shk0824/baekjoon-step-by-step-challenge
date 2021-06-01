a = set(range(1,10001))
b = set()
for i in range(1,10001):
    for x in str(i):
        i += int(x)
    b.add(i)
c = sorted(a - b)
for i in c:
    print(i)
