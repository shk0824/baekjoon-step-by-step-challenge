import sys

for raw_case in sys.stdin:
    for i in range(int(raw_case)):
        for input_test in sys.stdin:
            H,W,N=[int(x) for x in input_test.split()]
            Floor=N%H
            if Floor ==0: Floor=H
            Room=N//H
            if N%H!=0: Room+=1
            print(str(Floor)+(str(0)+str(Room))[-2:])
            break
