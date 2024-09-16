import sys

def arith_prog():
    n=int(sys.stdin.readline())
    if n<100: return n
    else:
        try:
            count=0
            for x in range(100,n+1):
                test=[int(i) for i in str(x)]
                change=test[0]-test[1]
                check=1
                for i in range(len(test)-1):
                    if test[i]-test[i+1]!=change:
                        check=0
                if check==1:
                    count+=1
        except:
            pass
    return count+99

print(arith_prog())
            
