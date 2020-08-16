n,*l=([*map(int,i.split())] for i in open(0)); l.sort(key=lambda x: (x[1],x[0])) #open으로 input을 받고 n에 맨 첫줄을 집어넣고 나머지 모두는 l에 넣기, sort()로 x[1]이 y값이니까 y값 정렬 후 같은 값이면 x값인 x[0]으로 정렬
for i in l:
    print(*i) # ,를 없애고  프린트
