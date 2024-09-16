""" def InviteDinnerOptimized(guestList, dislikePairs):
    n, invite = len(guestList), []
    for i in range(2**n):
        Combination = []
        num = ifor j in range(n):
        if (num % 2 == 1):
            Combination = [guestList[n-1-j]]+Combination
        num = num // 2
        good = True
        for j in dislikePairs:
            if j[0] in Combination and j[1] in Combination:
                good = False
        if good:
            if len(Combination) > len(invite):
                invite=Combination
    print('Optimum Solution: ', invite)
    """
def InviteDinnerOptimized(guestList, dislikePairs):
    badfriend=set() # 같이 있으면 안되는 친구 이름 리스트
    goodfriend=guestList.copy() #나중에 더할 항상 있어도 되는 친구 리스트

    for i in dislikePairs:
        badfriend.add(i[0])
        badfriend.add(i[1]) # 이름만 더하고 중복은 빼기
    badfriend=list(badfriend) #나중에 리스트끼리 더하기 위해 셋을 리스트로 바꾸기

    for i in guestList:
        for j in badfriend:
            if i[0]==j:
                goodfriend.remove(i) # 좋은 친구들만 걸러내기

    for i in goodfriend:
        guestList.remove(i) #이제 총 친구들 리스트에서 항상 들어갈 친구만 빼기

    n, invite, TotalScore = len(guestList), [], 0 #n은 사람 수, invite는 초대할 리스트, totalscore는 총 점수
    for i in range(2**n):
        Combination = []
        num = i
        score = 0
        for j in range(n): # 책에서 설명한 대로 0 부터 n까지의 수를 이진수로 표현하면서
            if (num % 2 == 1): # 밑에 자리부터 0 1 인지 확인하면서
                Combination = [guestList[n-1-j][0]]+Combination # 1이면 추가하고 0 이면 넘어가기
                score += guestList[n-1-j][1] # 만약 추가했으면 추가된 사람 점수도 더하기
            num = num // 2 # 윗자리수로 넘어가기 위해 2로 나눈 몫 num이 7이면 이진수는 00111 num //2 는 3 이고 또 3을 2 로 나누면 1 그다음 부터는 0,
        good=True
        for j in dislikePairs: #같이 있으면 안되는 페어가 있는지 확인
            if j[0] in Combination and j[1] in Combination:
                good=False
        if good:
            if score > TotalScore: #만약 토탈 점수보다 높으면 갱신
                TotalScore = score
                invite=Combination
            elif score == TotalScore and len(Combination) > len(invite): #점수가 같지만 또 인원수가 많다면 갱신
                invite=Combination

    for i in goodfriend: #마지막에 친구 더하기
        invite+=[i[0]]
    invite.sort()
    print('Optimum Solution: ', invite)


dislikePairs = [['B','C'],['C','D'],['D','E'],['F','G'],['F','H'],['F', 'H'],['F','I'],['G','H']]
guestList = [('A', 2), ('B', 1), ('C', 3), ('D', 2), ('E', 1),('F', 4),('G', 2),('H', 1),('I', 3)]

InviteDinnerOptimized(guestList, dislikePairs)
