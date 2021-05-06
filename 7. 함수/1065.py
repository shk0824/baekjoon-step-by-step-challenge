N = int(input())

def hansu(num):
    num = 0
    for i in range(1, N+1):
        if i < 100:
            num += 1
        elif i < 1000:
            a = i//100
            b = i%100//10
            c = i%100%10
            if (b-a) == (c-b):
                num += 1
    print(num)            

hansu(N)
