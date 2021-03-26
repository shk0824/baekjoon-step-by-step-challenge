# -*- coding: utf-8 -*-
""" 
    BIG_ICPC
    순천향대학교 빅데이터공학과
    20171483 한태규
    
    #------------------------- memo -------------------------#
    URL : https://www.acmicpc.net/step/2
    
    while문 정답 정리
    
    코드 문제 번호 : 10952, 10951, 1110
    #--------------------------------------------------------#
     
    email : gksxorb147@gmail.com
    update : 2021.03.22 19:55
"""




#--------------------------------------------------------#
# 10952 문제
# URL : https://www.acmicpc.net/problem/10952

while True:
    
    a = sum(map(int,input().split()))
    
    if a == 0: break

    print(a)

#--------------------------------------------------------#


#--------------------------------------------------------#
# 10951 문제
# URL : https://www.acmicpc.net/problem/10951 


while True:
    try: 
        a = sum(map(int,input().split()))
        print(a)
    except:
        break

    
#--------------------------------------------------------#


#--------------------------------------------------------#
# 1110 문제
# URL : https://www.acmicpc.net/problem/1110 

fst_num = input()

# 먼저 주어진 수가 10보다 작다면 
# 앞에 0을 붙여주기
if int(fst_num) < 10: 
    fst_num = "0" + fst_num

a, b = tuple(fst_num)

cycle = 0

while True:
    
    cycle += 1
    
    sum_num = str(int(a) + int(b))
    #print("sum_num : " + sum_num)
    
    new_num = str(b + sum_num[-1])
    #print("new_num : " + new_num)
    
    if str(new_num) == fst_num:
        break
    
    a, b = tuple(new_num)
    
print(cycle)

#--------------------------------------------------------#