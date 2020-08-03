while 1:
    n=int(input())
    if n==-1: break
    r_answer="1"
    sum=1
    for i in range(2,n):
        if n%i==0:
            r_answer+=f" + {i}"
            sum+=i
    if sum==n:
        print(n,"=",r_answer)
    else: print(n,"is NOT perfect.")
