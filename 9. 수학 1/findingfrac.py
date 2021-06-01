nth=1 #열 혹은 행의 위치, 1부터 시작
sumdiag=2 # 각 대각선의 합, 첫 대각선의 합은 2 분자와 분모의 합
direction=1 # 이것은 지그재그가 아래로 향하는지 아니면 위로 향하는지 확인 1이면 +라서 위로 -1이면 -라서 아래로
diaglastnth=1 #각 대각선을 따라갔을 때 벽이랑 부딪히는 마지막 숫자, 이것으로 input이 어디 대각선에 위치한지 비교

x=int(input())

while True:
    if x<=diaglastnth: #만약에 x가 어떠한 대각선 마지막에 위치한 숫자보다 같거나 작으면(처음 dialastnth는 1이니까 
                             #계속 diaglastnth를 키워나가면서 x보다 같거나 큰 diaglastnth를 만난다)
        xth=diaglastnth-x #xth는 diaglastnth와 x의 차이로 대각선 끝에서 몇번째 떨어져있는지에 관한 수
        if direction>0: #만야게 direction이 1이라서 방향이 위로 향하면 분모와 분자의 줄어들거나 커지는 것을 정한다.
            nom=1+xth #위로 향하면 분자는 1에서 떨어진만큼 올라가고
            denom=nth-xth #분모는 행의 위치에서 n만큼 줄어든다. 행이 올라가는 방식
        else: #반대로 생각해서 방향이 내려가면 열인 분자는 xth 만큼씩 현재 열 위치에서 줄어들고 분모는 1에서 커진다.
            nom=nth-xth
            denom=1+xth
        break
    else: #만약 x가 diaglastnth보다 커서 그 다음 대각선으로 넘어가서 확인해야하면
        nth+=1 #열 혹은 행 위치를 한칸 올리고(한칸 올라간 뒤의 현재열)
        sumdiag+=1 #각 대각선의 합을 1 올리고, 대각선 합은 대각선이 올라갈 때마다 1씩 증가
        direction*=-1 #방향은 처음에는 올라가는 것으로 시작해서 내려갔다가 올라갔다가 계속 반복한다.
        diaglastnth+=nth #각 대각선의 마지막 숫자는 그 전 열들과 현재 열 위치 숫자를 더한 값이다.
print(f"{nom}/{denom}")
