import sys


for number in sys.stdin:
    input_num=int(number)
    n=0
    max_in_the_group=1
    while True:
        if input_num<=max_in_the_group: print(n+1); break
        else: n+=1; max_in_the_group+=(6*n)
