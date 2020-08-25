N,M=map(int,input().split())
visited=[0]*(N+1) #DFS 처럼 사용하면 1로 만들어서 체크, 나올 때 다시 0
tmp=[0]*M # 다른 코드 보니까 arr로 수열 갯수가 문제 조건에 충족하면 프린트하도록 하기 위해서 일회용 리스트
def pn(n,m,d):
    global tmp

    if (d==m): # 만약에 수열만큼 숫자가 tmp에 채워지면 tmp 안에 있는 것 프린트
        if tmp==sorted(tmp): #만약 tmp인자가의 순서가 오름차순이라면
            for i in tmp:
                    print(i, end=" ")
            print()
        return

    for i in range(1,n+1): #1 부터 n까지 각각 한개씩 넣고
        if not visited[i]: # visited가 1이 아니면
            visited[i]=1 #visited 1로 만들고
            tmp[d]=i #tmp의 d번째 수열에 숫자 입력하고
            pn(n,m,d+1) #여기서 부터 다시 위에 부분 반복
            visited[i]=0 #반복해서 안쪽 사이클 다 돌고 바깥쪽으로 나와서 visited를 0으로 바꿔서 들어갔다가 나와서 나온 숫자를 다시 사용할 수 있도록 하기 위해
    return

pn(N,M,0)
