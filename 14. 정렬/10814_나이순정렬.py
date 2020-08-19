n,*j=([*i.split()] for i in open(0)) #i.split()으로 open(0)로 받은 각 줄을 각각 리스트로 바꿔서 처음꺼는 n에 나머지 모두는 j에 넣기
j.sort(key=lambda x: int(x[0])) #sort()로 각 리스트 첫번째 나이를 int 변환 후 키로서 정렬
for i in j:
    print(*i) #한 줄에 j 리스트 안에 있는 각각의 i 리스트의 개체를 띄워서 프린트 
