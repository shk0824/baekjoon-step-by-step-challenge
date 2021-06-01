#1번

def bisectionSearchForSquareRoot(x, epsilon):
    if x < 0:
        print ('Sorry, imaginary numbers are out of scope!')
        return
    numGuesses = 0
    if x <1:
        low = x
        high = 1
    else:
        low = 0.0
        high = x
    ans = (high +low)//2
    while abs(ans**2 - x)>=epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
        numGuesses +=1
    print('numGuesses = ', numGuesses)
    print(ans, 'is close to square root of',x)

bisectionSearchForSquareRoot(0.25,0.01)

#2번

def bsearch(L, value, gap):
    lo, hi = 0, len(L)-1
    while lo <=hi:
        if hi-lo < gap:
            for i in range(lo,hi+1):
                if L[i]==value:
                    return i
        else: 
            mid = (lo +hi) // 2
            if L[mid] < value:
                lo = mid +1
            elif value < L[mid]:
                hi = mid -1
            else:
                print (mid+1)
                return
    return "NOTFOUND"

Ls=[2,3,5,7,11,13,17,23,29,31,37,41,43,47,53,59,61,67,71,73,7,83,89,97]
bsearch(Ls, 29,3)


#3번

def func(x):
    return(x**3 +x**2-11) # 해를 찾을 다항식

def bsearchroot(start,end,epsilon):
    l=start; r=end; ep= epsilon
    mid=(l+r)//2
    while abs(func(mid)) >=ep:
        mid = (l+r)/2
        if func(mid) < 0:
            l =  mid
        elif func(mid) > 0:
            r = mid
        else:
            return mid
    return mid

for i in range(int(input())): #테스트 케이스 개수
    start,end,epsilon=[float(x) for x in input().split()] # x축 교차구간 및 오차범위
    start=int(start);end=int(end)

    print("the nearest root is",bsearchroot(start,end,epsilon))
