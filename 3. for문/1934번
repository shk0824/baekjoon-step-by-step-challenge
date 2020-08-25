N = int(input())
for n in range(N):
    A, B = map(int, input().split())
    if A >= B:
        A, B = B, A
    gcd = 0
    for m in range(A,0, -1):
        if A % m == 0 and B % m == 0:
           gcd = m
           break
    lcm = (A * B) // gcd 
    print(lcm)
