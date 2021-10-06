def Hire4Show(candList, candTalents, talentList):
    candList2=candList.copy() # 마지막에 출력형식을 맞추기 위해 입력리스트 복사
    candname=[]#이름만 추출
    for i in candList:
        candname.append(i[0])
    candscore=[] # 점수만 추출
    for i in candList:
        candscore.append(i[1])

    candList=candname # 리스트에 이름만 넣기
    n = len(candList) # 총 후보자 수

    subsetList = [] # 부분집합으로 속하는 후보자들의 집합
    for i in range(n):
        compare=candTalents[i] # 비교할 후보자
        for j in range(n):
            if i == j: # 비교할 사람이 서로 같으면 패스
                continue
            if j in subsetList: # 비교할 대상이 벌써 그 전에 비교되어서 사라진 것이라면 패스
                continue
            to_compare=candTalents[j] # 비교할 상대
            if len(compare) <=len(to_compare): #비교할 후보자의 원소 개수가 같거나 작을 때만 확인하기
                count=0
                for tal in compare:
                    if tal in to_compare:
                        count+=1 # 비교할 후보자의 장기가 다 포함될 때 count 는 후보자의 탤런트 개수와 같다
                if count == len(compare):
                    if candscore[j] <= candscore[i]: #만약 비교되는 후보자가 비교할 상대보다 점수가 크거나 같을 때만 지우도록
                        subsetList+=[i] # 만약 같다면 위의 부분 집합 안에 추가
                        break # 이제 찾았으니 i 번째 비교는 끝내기

    n = n - len(subsetList) # 부분집합 후보자 빼고 남은 후보자들 수

    for i in subsetList: # 부분집합에 들어가 있는 후보자들 빼기
        candList[i]=None
        candTalents[i]=None
        candscore[i]=None # 스코어도 지우기
    candList=list(filter(None,candList))
    candscore=list(filter(None,candscore))
    candTalents=list(filter(None,candTalents))


    ## 2번 문제 코드 변형
    uniqueset=[] # 탤런트를 가진 유일한 후보자 집합
    table=[] # 탤런트와 후보자간 매칭 테이블
    for i in range(n): # 한 사람씩 루프
        tmp=[] # 각 사람 정보 담을 일시적인 리스트
        for j in talentList: # 각 탤런트를 돌면서 만약 그 후보가 탤런트 가지고 있으면 1 아니면 0 넣기
            if j in candTalents[i]:
                tmp+=[1]
            else: tmp+=[0]
        table.append(tmp) # 최종으로 붙이기

    uniqueList=[] # 탤런트 중에서 한개만 있는 것을 찾기
    for i in range(len(talentList)): #탤런트 숫자만큼 루프를 돌면서
        count=0
        for j in range(n): # 사람마다 가지고 있는 탤런트를 체크
            count+=table[j][i] #탤런트가 존재하는 수 더하기
        uniqueList+=[count]


    for i in range(len(talentList)):
        if uniqueList[i] == 1: #만약 탤런트가 하나뿐이라면 유일한 후보자가 있기 때문에 후보자 찾기
            for j in range(n):
                if talentList[i] in candTalents[j]:
                    uniqueset+=[j] #j번째 후보자 추가
    uniqueset=set(uniqueset) # 후보자 중에 유일한 탤런트 두개를 가진 후보자가 있을 수 있으니 중복된 후보자 제거

    for cand in uniqueset:

        for talent in candTalents[cand]:
            if talent in talentList: # 탤런트 리스트에서도 빼기
                talentList.remove(talent)

    n = n - len(uniqueset) # 부분집합 후보자 빼고 남은 후보자들 수

    uniqueCandandTalent={} #나중에 추가할 정보담을 딕셔너리
    uniquescore=0
    for i in uniqueset: # 부분집합에 들어가 있는 후보자들 빼기
        uniqueCandandTalent[candList[i]]=candTalents[i] # 아이디와 값으로 넣기
        uniquescore+=candscore[i] #유니크 후보자의 점수도 따로 저장
        candscore[i]=None #스코어지우기
        candList[i]=None
        candTalents[i]=None

    candscore=list(filter(None,candscore))
    candList=list(filter(None,candList))
    candTalents=list(filter(None,candTalents))

    #3번

    TotalScore=sum(candscore)


    hire = candList[:]
    for i in range(2**n):
        score=0
        Combination = []
        num = i
        for j in range(n):
            if (num % 2 == 1):
                score+=candscore[n-1-j]
                Combination = [candList[n-1-j]] + Combination
            num = num // 2
        if Good(Combination, candList, candTalents, talentList):
            if score < TotalScore: #조합의 길이가 아닌 점수로 최적의 조합 찾기
                hire = Combination
                TotalScore=score #스코어 갱신
    for uniqueCand in uniqueCandandTalent:
        hire+=[uniqueCand] #마지막에 유일한 탤런트 가진 후보자 더하기
    TotalScore+=uniquescore # 위에서 뺐던 유니크 후보자 점수 더하기
    result=[]
    for j in candList2:
        if j[0] in hire:
            result.append(j) #출력형식 맞추기
    print ('Optimum Solution: ', result, "\nWeight is: ", TotalScore)

def Good(Comb, candList, candTalents, AllTalents):
    for tal in AllTalents:
        cover = False
        for cand in Comb:
            candTal = candTalents[candList.index(cand)]
            if tal in candTal:
                cover = True
        if not cover:
            return False
    return True

Talents = ['Sing', 'Dance', 'Magic', 'Act', 'Flex', 'Code']
Candidates = ['Aly', 'Bob', 'Cal', 'Don', 'Eve', 'Fay']
CandidateTalents = [['Flex','Code'], ['Dance', 'Magic'], ['Sing', 'Magic'], ['Sing', 'Dance'], ['Dance', 'Act', 'Code'], ['Act', 'Code']]

ShowTalent2 = [1,2,3,4,5,6,7,8,9]
CandidateList2=['A','B','C','D','E','F','G']
CandToTalents2=[[4,5,7],[1,2,8],[2,4,6,9],[3,6,9],[2,3,9],[7,8,9],[1,3,7]]


#Hire4Show(Candidates, CandidateTalents, Talents)
#Hire4Show(CandidateList2, CandToTalents2, ShowTalent2)

ShowTalentW = [1,2,3,4,5,6,7,8,9]
CandidateListW = [ ('A', 3), ('B', 2), ('C', 1), ('D', 4), ('E', 5), ('F', 2), ('G', 7)]
CandToTalentsW = [[1,5], [1,2,8], [2,3,6,9], [4,6,8], [2,3,9],[7,8,9],[1,3,5]]

Hire4Show(CandidateListW, CandToTalentsW, ShowTalentW)