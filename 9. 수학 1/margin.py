import sys


for x in sys.stdin:    
    f_cost, p_cost, price=[int(y) for y in x.split()]
    if f_cost+2*p_cost-2*price-f_cost+p_cost-price>=0: 
        sys.stdout.write("-1")
    else:
        count= f_cost//(price-p_cost)+1
        sys.stdout.write(str(count)+"\n")
