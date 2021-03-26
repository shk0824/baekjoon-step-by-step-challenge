# -*- coding: utf-8 -*-
""" 
    BIG_ICPC
    순천향대학교 빅데이터공학과
    20171483 한태규
    
    #------------------------- memo -------------------------#
    URL : https://www.acmicpc.net/step/3
    
    for문 정답 정리
    
    코드 문제 번호 : 2739, 10950, 8393, 15552, 2741
                  , 2742, 11021, 11022, 2438, 2439
                  , 10871
    #--------------------------------------------------------#
     
    email : gksxorb147@gmail.com
    update : 2021.03.26 18:54
"""




# #--------------------------------------------------------#
# 2739 문제
# URL : https://www.acmicpc.net/problem/2739

a = int(input())

for n in range(1,10):
    print("{} * {} = {}".format(a, n, n*a))
    
# #--------------------------------------------------------#


# #--------------------------------------------------------#
# 10950 문제
# URL : https://www.acmicpc.net/problem/10950

for n in range(int(input())): 
    print(sum(map(int,input().split()))) 
    
    # 1 1
    
    # input().split() > ['1', '1']
    
    # map(int,input().split()) > <map object at 0x0000028726D08460>
    
    # sum(map(int,input().split())) > 2
    
# #--------------------------------------------------------#


# #--------------------------------------------------------#
# 8393 문제
# URL : https://www.acmicpc.net/problem/8393

print(sum([ n for n in range(int(input()) + 1) ]))

    # range(int(input()) + 1) > range(0, 4)

    # [ n for n in range(int(input()) + 1) ] > [0, 1, 2, 3]
    
    # sum([ n for n in range(int(input()) + 1) ]) > 6

# #--------------------------------------------------------#


# #--------------------------------------------------------#
# 15552 문제
# URL : https://www.acmicpc.net/problem/15552

import sys

for n in range(int(input())):
    print(sum(map(int, sys.stdin.readline().strip().split())))
    
    # 12 34
    
    # sys.stdin.readline().strip() > '12 34'
    
    # sys.stdin.readline().strip().split() > ['12', '34']
    
    # map(int, sys.stdin.readline().strip().split()) > <map object at 0x0000028726BF3700>
    
    # sum(map(int, sys.stdin.readline().strip().split())) > 46

# #--------------------------------------------------------#


# #--------------------------------------------------------#
# 2741 문제
# URL : https://www.acmicpc.net/problem/

for n in range(1, int(input()) + 1):
    print(n)
    
# #--------------------------------------------------------#


# #--------------------------------------------------------#
# 2742 문제
# URL : https://www.acmicpc.net/problem/2742

for n in range(int(input()), 0, -1):
    print(n)

# #--------------------------------------------------------#


# #--------------------------------------------------------#
# 11021 문제
# URL : https://www.acmicpc.net/problem/11021

for n in range(int(input())): 
    
    n_sum = sum(map(int,input().split()))
    print("Case #{}: {}".format(n + 1, n_sum))

# #--------------------------------------------------------#


# #--------------------------------------------------------#
# 11022 문제
# URL : https://www.acmicpc.net/problem/11022

for n in range(int(input())): 
    
    a, b = tuple(map(int,input().split()))
    n_sum = a + b
    
    print("Case #{}: {} + {} = {}".format( n + 1
                                          , a
                                          , b
                                          , n_sum ))

# #--------------------------------------------------------#


# #--------------------------------------------------------#
# 2438 문제
# URL : https://www.acmicpc.net/problem/2438

for n in range(int(input())): 
    print("*"*(n + 1))

# #--------------------------------------------------------#


# #--------------------------------------------------------#
# 2439 문제
# URL : https://www.acmicpc.net/problem/2439

st_nubmer = int(input())

for n in range(0, st_nubmer): 
    
    start_gap = (st_nubmer - (n + 1))*' '
    start_str = '*'*(n + 1)
    
    print(start_gap + start_str)

# #--------------------------------------------------------#


# #--------------------------------------------------------#
# 10871 문제
# URL : https://www.acmicpc.net/problem/10871

a, b = tuple(map(int,input().split()))
num_list = map(int,input().split())

for n in num_list:
    if n < b:
        print(n, end=" ")

# #--------------------------------------------------------#