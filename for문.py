구구단 (1)
#2X1=2

n =int(input())

for i in range(1,10):
    print('{0} * {1} = {2}'.format(n, i,n * i))





A+B (2)
t = int(input())

while t:
    t -=1
    
    a,b = list(map(int, input().split()))
    print(a + b)
----------------------------------------------
test_case = int(input())

for _ in range(test_case):
    input_data = input().split(' ')
    A = int(input_data[0])
    B = int(input_data[1])
    print(A + B)





1~n 합 (3)
n = int(input())

print(n * (n+1) // 2)
---------------------------------
sum = 0

n = int(input())

for i in range(1, n + 1):
    sum += i

print(sum)





빠른 a+b (4)
import sys

input = sys.stdin.readline

t = int(input())

while t:
    t -= 1
    
    a, b=list(map(int, input().split()))
    print(a + b)

-------------------------------------------
import sys

test_case = int(input())

for _ in range(test_case):
    input_data = sys.stdin.readline().rstrip().split(' ')
    A = int(input_data[0])
    B = int(input_data[1])
    print(A + B)





n 찍기 (5)
n = int(input())

for a in range(1,n+1):
    print(a)

-----------------------------------------
n = int(input())

for i in range(1, n + 1):
    print(i)





n 찍기 (거꾸로) (6)
    n = int(input())

for a in range(n, 0, -1): 
    print(a)

------------------------------------------
n = int(input())

#n~1
for i in range(n, 0, -1):
    print(i)





A+B-7      (7)
import sys

input = sys.stdin.readline

t = int(input())

for i in range(1, t + 1):
    a, b = list(map(int, input().split()))
    print(f"Case #{i}: {a} + {b} = {a+b}")

A+B-8 (생략,8)





별 찍기 (9)
n = int(input())

for i in range(1, n + 1):
    for j in range(0, i):
        print('*', end='')
    print()


별 찍기(10) 생략

x 보다 작은 수 (11)
input_data = input().split(' ')
n = int(input_data[0])
x = int(input_data[1])

#1 5 4 3
# ['1', '5', '3', '4']
# [1, 5, 4, 3]
a = list(map(int, input().split(' ')))

# 1 5 4 3
for i in a:
    if x > i:
        print(i)
        


