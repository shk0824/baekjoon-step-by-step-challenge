import sys


for number in sys.stdin:
    sugar=int(number)
    if sugar in [1,2,4,7]: print(-1)
    elif sugar%5==0: print(sugar//5)
    elif (sugar%5)%2==0: print((sugar//5)+2)
    elif (sugar%5)%2==1: print((sugar//5)+1)
                
