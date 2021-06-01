###연습문제 1,2,3번을 모두 포함한 코드입니다.

def findthefloor(n,d):
    r = 1
    while r**d<n: 
        r+=1
    if r**(d-1)*(d-1)>=n:
        d-=1
    print("radix chosen is",r)
    
    FloortoCheck=[0]*d
    numdrop = 0
    ballused=1
    startfloor=0
    endfloor=n
    neednewball=False

    for i in range(d):
        for j in range(r-1):
            FloortoCheck[i]+=1
            Floor = ConverttoDecimal(d,r,FloortoCheck)
            if Floor > n:
                FloortoCheck[i] -=1
                break
            else:
                if neednewball:
                    ballused+=1
                print("check floor","[",startfloor,",",endfloor,"]")
                print("Drop the ball",ballused," on floor", Floor)
                numdrop+=1
                yes=input("Did the ball break? yes/no :")
                if yes =="yes":
                    neednewball=True
                    endfloor=Floor-1
                    FloortoCheck[i]-=1
                    break
                else:
                    neednewball=False
                    startfloor=Floor+1
    Floor=ConverttoDecimal(d,r,FloortoCheck)
    
    print("the ball is safe until floor",Floor,"and found it by dropping",ballused,"ball(s)",numdrop,"times.")

def ConverttoDecimal(d,r,rep):
    number = 0 
    for i in range(d-1):
        number=(number + rep[i])*r
    number+=rep[-1]
    return number

if __name__=="__main__":
    n=int(input("how many floors? "))
    d=int(input("how many beads? "))
    findthefloor(n,d)
