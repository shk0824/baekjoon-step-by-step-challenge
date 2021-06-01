deck = ['A_C','A_D','A_H','A_S','2_C','2_D','2_H','2_S',
        '3_C','3_D','3_H','3_S','4_C','4_D','4_H','4_S',
        '5_C','5_D','5_H','5_S','6_C','6_D','6_H','6_S',
        '7_C','7_D','7_H','7_S','8_C','8_D','8_H','8_S',
        '9_C','9_D','9_H','9_S','10_C','10_D','10_H','10_S',
        'J_C','J_D','J_H','J_S','Q_C','Q_D','Q_H','Q_S',
        'K_C','K_D','K_H','K_S']
###교재 코드###
def AssistantOrdersCards():
    print('Cards are chracter strings as shown below.')
    print('Ordering is:',deck)
    cards,cind,cardsuits,cnumbers=[],[],[],[]
    numsuits=[0,0,0,0]
    for i in range(5):
        print('Please give card', i+1, end = ' ')
        card=input('in above format:')
        cards.append(card)
        n=deck.index(card)
        cind.append(n)
        cardsuits.append(n%4)
        numsuits[n%4]+=1
        if numsuits[n%4]>1:
            pairsuit=n%4
    cardh=[]
    for i in range(5):
        if cardsuits[i]==pairsuit:
            cardh.append(i)
    hidden,other,encode =\
    outputFirstCard(cnumbers,cardh,cards)
    remindices = []

    for i in range(5):
        if i != hidden and i != other:
            remindices.append(cind[i])
    sortList(remindices)
    outputNext3Cards(encode, remindices)
    return

def outputFirstCard(ns, oneTwo, cards):
    encode = (ns[oneTwo[0]]-ns[oneTwo[1]])%13
    if encode > 0 and encode <=6:
        hidden = oneTwo[0]
        other = oneTwo[1]
    else:
        hidden = oneTwo[1]
        other = oneTwo[0]
        encode=(ns[oneTwo[1]]-ns[oneTwo[0]])%13
    print('First card is:', cards[other])
    return hidden, other, encode

def outputNext3Cards(code, ind):
    if code == 1:
        s, t, f = ind[0], ind[1], ind[2]
    elif code ==2:
        s, t, f = ind[0], ind[2], ind[1]
    elif code ==3:
        s, t, f = ind[1], ind[0], ind[2]
    elif code == 4:
        s, t, f = ind[1], ind[2], ind[0]
    elif code == 5:
        s, t, f = ind[2], ind[0], ind[1]
    else:
        s, t, f = ind[2], ind[1], ind[0]
    print ('Second card is:', deck[s])
    print ('Third card is:', deck[t])
    print ('Fourth card is', deck[f])

def sortList(tlist):
    for ind in range(0,len(tlist)-1):
        iSm = ind
        for i in range(ind,len(tlist)):
            if tlist[iSm] > tlist[i]:
                iSm=i
        tlist[ind], tlist[iSm] = tlist[iSm], tlist[ind]
    return tlist

def MagicianGuessCard():
    print ('Cards are character strings as shown below')
    print ('Ordering is:', deck)
    cards, cind = [], []
    for i in range(4):
        print ('Please give card', i+1, end = ' ')
        card = input('in above format:')
        cards.append(card)
        n=deck.index(card)
        cind.append(n)
        if i ==0:
            suit = n%4
            number = n//4
    if cind[1] < cind[2] and cind[1] < cind[3]:
        if cind[2] < cind[3]:
            encode = 1
        else:
            encode = 2
    elif ((cind[1] > cind[2] and cind[1] < cind[3]) 
        or (cind[1] < cind[3] and cind[1] > cind[3])):
        if cind[2] < cind[3]:
            encode = 3
        else:
            encode = 4
    elif cind[1] > cind[2] and cind[1] > cind[3]:
        if cind[2] < cind[3]:
            encode = 5
        else:
            encode = 6
    hiddennumber = (number + encode) % 13 
    index = hiddennumber * 4 + suit
    print ('Hidden card is:', deck[index])
###1번  ###
def ComputerAssistant1():
    print('Cards are character strings as shown below.')
    print('Ordering is:', deck)
    cards, cind, cardsuits, cnumbers = [], [], [], []
    numsuits = [0, 0, 0, 0]
    number = int(input('Please give random number of' + 'at least 6 digits:'))
    randlist=[]
    check=True
    while check: # WHILE문 사용하여 boolean check 조건을 걸어서 중복되는 n 이 생길 경우 정지하고 다시 number를 1만큼 키워서 새로운 카드 추출하기
        check=False
        cards, cind, cardsuits, cnumbers = [], [], [], []
        numsuits = [0, 0, 0, 0]
        randlist=[]
        for i in range(5):
            number= number*(i+1)//(i+2)
            n=number%52
            if n in randlist:
                check=True
                number+=1
                break
            randlist+=[n]
            cards.append(deck[n])
            cind.append(n)
            cardsuits.append(n%4)
            cnumbers.append(n//4)
            numsuits[n%4]+=1
            if numsuits[n%4]>1:
                pairsuit = n%4

    cardh=[]
    for i in range(5):
        if cardsuits[i]==pairsuit:
            cardh.append(i)
    hidden,other,encode =\
    outputFirstCard(cnumbers,cardh,cards)
    remindices = []

    for i in range(5):
        if i != hidden and i != other:
            remindices.append(cind[i])
    sortList(remindices)
    outputNext3Cards(encode, remindices)
    
    guess=input('What is the hidden card?')
    if guess == cards[hidden]:
        print("You are a Mind Reader Extraordinaire")
    else:
        print('Opps, please retry~')
    

####2번###

def ComputerAssistant2():
    print('Cards are character strings as shown below.')
    print('Ordering is:', deck)
    cards, cind, cardsuits, cnumbers = [], [], [], []
    numsuits = [0, 0, 0, 0]
    number = int(input('Please give random number of' + 'at least 6 digits:'))
    randlist=[]
    check=True
    while check: # WHILE문 사용하여 boolean check 조건을 걸어서 중복되는 n 이 생길 경우 정지하고 다시 number를 1만큼 키워서 새로운 카드 추출하기
        check=False
        cards, cind, cardsuits, cnumbers, pairsuit = [], [], [], [], []
        numsuits = [0, 0, 0, 0]
        randlist=[]
        for i in range(5):
            number= number*(i+1)//(i+2)
            n=number%52
            if n in randlist:
                check=True
                number+=1
                break
            randlist+=[n]
            cards.append(deck[n])
            cind.append(n)
            cardsuits.append(n%4)
            cnumbers.append(n//4)
            numsuits[n%4]+=1
    pickpair=[13,13,13,13]
    for i in range(4):
        pair=[]
        if numsuits[i]>1:
            for p in range(5):
                if cardsuits[p]==i:
                    pair+=[p]
            if len(pair)==3:
                p01=min(((cnumbers[pair[0]]-cnumbers[pair[1]])%13),((cnumbers[pair[1]]-cnumbers[pair[0]])%13))
                p02=min(((cnumbers[pair[0]]-cnumbers[pair[2]])%13),((cnumbers[pair[2]]-cnumbers[pair[0]])%13))
                p12=min(((cnumbers[pair[1]]-cnumbers[pair[2]])%13),((cnumbers[pair[2]]-cnumbers[pair[1]])%13))
                pmin=min(p01,p02,p12)
                pickpair[i]=pmin
            else:
                p01=min(((cnumbers[pair[0]]-cnumbers[pair[1]])%13),((cnumbers[pair[1]]-cnumbers[pair[0]])%13))
                pickpair[i]=p01
    pairsuit=pickpair.index(min(pickpair))                      

    cardh=[]
    for i in range(5):
        if cardsuits[i]==pairsuit:
            cardh.append(i)
    hidden,other,encode =\
    outputFirstCard(cnumbers,cardh,cards)
    remindices = []

    for i in range(5):
        if i != hidden and i != other:
            remindices.append(cind[i])
    sortList(remindices)
    outputNext3Cards(encode, remindices)
    
    guess=input('What is the hidden card?')
    if guess == cards[hidden]:
        print("You are a Mind Reader Extraordinaire")
    else:
        print('Opps, please retry~')

# ComputerAssistant2()

###3번 ###
deck3 = ['A_C', '2_C','3_C','4_C','5_C','6_C','7_C','8_C','9_C','10_C',
        'J_C','Q_C','K_C','A_D','2_D','3_D','4_D','5_D','6_D','7_D','8_D','9_D','10_D',
        'J_D','Q_D','K_D','A_H','2_H','3_H','4_H','5_H','6_H','7_H','8_H','9_H','10_H','J_H','Q_H','K_H',
        'A_S','2_S','3_S','4_S','5_S','6_S','7_S','8_S','9_S','10_S','J_S','Q_S','K_S']

def ComputerAssistant3():
    print('Cards are character strings as shown below.')
    print('Ordering is:', deck3)
    cards, cind, cardsuits, cnumbers = [], [], [], []
    numsuits = [0, 0, 0, 0]
    number = int(input('Please give random number of' + 'at least 6 digits:'))
    randlist=[]
    check=True
    while check: # WHILE문 사용하여 boolean check 조건을 걸어서 중복되는 n 이 생길 경우 정지하고 다시 number를 1만큼 키워서 새로운 카드 추출하기
        check=False
        cards, cind, cardsuits, cnumbers, pairsuit = [], [], [], [], []
        numsuits = [0, 0, 0, 0]
        randlist=[]
        for i in range(5):
            number= number*(i+1)//(i+2)
            n=number%52
            if n in randlist:
                check=True
                number+=1
                break
            randlist+=[n]
            cards.append(deck3[n])
            cind.append(n)
            cardsuits.append(n//13)
            cnumbers.append(n%13)
            numsuits[n//13]+=1
    pickpair=[13,13,13,13]
    for i in range(4):
        pair=[]
        if numsuits[i]>1:
            for p in range(5):
                if cardsuits[p]==i:
                    pair+=[p]
            if len(pair)==3:
                p01=min(((cnumbers[pair[0]]-cnumbers[pair[1]])%13),((cnumbers[pair[1]]-cnumbers[pair[0]])%13))
                p02=min(((cnumbers[pair[0]]-cnumbers[pair[2]])%13),((cnumbers[pair[2]]-cnumbers[pair[0]])%13))
                p12=min(((cnumbers[pair[1]]-cnumbers[pair[2]])%13),((cnumbers[pair[2]]-cnumbers[pair[1]])%13))
                pmin=min(p01,p02,p12)
                pickpair[i]=pmin
            else:
                p01=min(((cnumbers[pair[0]]-cnumbers[pair[1]])%13),((cnumbers[pair[1]]-cnumbers[pair[0]])%13))
                pickpair[i]=p01
    pairsuit=pickpair.index(min(pickpair))                      

    cardh=[]
    for i in range(5):
        if cardsuits[i]==pairsuit:
            cardh.append(i)
    hidden,other,encode =\
    outputFirstCard3(cnumbers,cardh,cards)
    remindices = []

    for i in range(5):
        if i != hidden and i != other:
            remindices.append(cind[i])
    sortList(remindices)
    outputNext3Cards3(encode, remindices)
    
    guess=input('What is the hidden card?')
    if guess == cards[hidden]:
        print("You are a Mind Reader Extraordinaire")
    else:
        print('Opps, please retry~')

def outputFirstCard3(ns, oneTwo, cards):
    encode = (ns[oneTwo[0]]-ns[oneTwo[1]])%13
    if encode > 0 and encode <=6:
        hidden = oneTwo[0]
        other = oneTwo[1]
    else:
        hidden = oneTwo[1]
        other = oneTwo[0]
        encode=(ns[oneTwo[1]]-ns[oneTwo[0]])%13
    print('First card is:', cards[other])
    return hidden, other, encode

def outputNext3Cards3(code, ind):
    if code == 1:
        s, t, f = ind[0], ind[1], ind[2]
    elif code ==2:
        s, t, f = ind[0], ind[2], ind[1]
    elif code ==3:
        s, t, f = ind[1], ind[0], ind[2]
    elif code == 4:
        s, t, f = ind[1], ind[2], ind[0]
    elif code == 5:
        s, t, f = ind[2], ind[0], ind[1]
    else:
        s, t, f = ind[2], ind[1], ind[0]
    print ('Second card is:', deck3[s])
    print ('Third card is:', deck3[t])
    print ('Fourth card is', deck3[f])

#ComputerAssistant3()

###4번 ###

def ComputerAssistant4Cards():
    print('Cards are character strings as shown below.')
    print('Ordering is:', deck)
    cards, cind, cardsuits, cnumbers = [], [], [], []
    numsuits = [0, 0, 0, 0]
    number = int(input('Please give random number of' + 'at least 6 digits:'))
    randlist=[]
    check=True
    while check: # WHILE문 사용하여 boolean check 조건을 걸어서 중복되는 n 이 생길 경우 정지하고 다시 number를 1만큼 키워서 새로운 카드 추출하기
        check=False
        cards, cind, cnumbers, cardsuits, Folded = [], [], [], [], True
        randlist=[]
        for i in range(4):
            number= number*(i+1)//(i+2)
            n=number%52
            if n in randlist:
                check=True
                number+=1
                break
            randlist+=[n]
            cards.append(deck[n])
            cind.append(n)
            cardsuits.append(n%4)
            cnumbers.append(n//4)
    for i in range(4):
        for p in range(3-i):
            distance=min((cind[i]-cind[i+p+1])%52,(cind[i+p+1]-cind[i])%52)  #여기서 각 카드의 전체 거리가 52칸이라서 시계방향 거리, 
            if (distance <= 13) and (distance >= -13):                      #반대방향 거리를 52 모듈로 연산을 하여 제일 낮은 값을 거리로 하게 되면 
                cardh=[i,i+p+1]                                             #무조건 한 페어는 최대 13의 거리를 가지게 될 것이다.
                break
    [1,51,15,29]
    hidden,other,encode,left,right =\
    outputFirstin4Cards(cind,cardh,cards,cind
    )    
    guess=input('What is the hidden card?')
    if guess == cards[hidden]:
        print("You are a Mind Reader Extraordinaire")
    else:
        print('Opps, please retry~')
        print(cards[hidden])


def outputFirstin4Cards(ns, oneTwo, cards,cind):
    encode = (ns[oneTwo[0]]-ns[oneTwo[1]])%52
    Left=Right=0
    if encode > 0 and encode <=13:
        hidden = oneTwo[0]
        other = oneTwo[1]
    else:
        hidden = oneTwo[1]
        other = oneTwo[0]
        encode=(ns[oneTwo[1]]-ns[oneTwo[0]])%52
    
    remindices = []

    for i in range(4):
        if i != hidden:
            remindices.append(cind[i])

    remindices=sortList4Cards(remindices)

    code=encode
    ind=remindices

    if code>6:
        code-=6
    if code == 1:
        s, t, f = ind[0], ind[1], ind[2]
    elif code ==2:
        s, t, f = ind[0], ind[2], ind[1]
    elif code ==3:
        s, t, f = ind[1], ind[0], ind[2]
    elif code == 4:
        s, t, f = ind[1], ind[2], ind[0]
    elif code == 5:
        s, t, f = ind[2], ind[0], ind[1]
    else:
        s, t, f = ind[2], ind[1], ind[0]
    
    if code==7:
        otherside='Right'
        elseside='Left'
    else:
        otherside='Left'
        elseside='Right'

    print ('First card is:', deck[s],end=' ')
    if s==cind[other]:
        print("on the", otherside)
    else: print("on the", elseside)
    print ('Second card is:', deck[t],end=' ')
    if t==cind[other]:
        print("on the", otherside)
    else: print("on the", elseside)
    print ('Third card is', deck[f],end=' ')
    if f==cind[other]:
        print("on the", otherside)
    else: print("on the", elseside)
    if encode>6: 
        print('All other cards are Folded Down')
    else: print('All other cards are shown upward')
    return hidden, other, encode, Left, Right

def sortList4Cards(tlist):
    for ind in range(0,len(tlist)-1):
        iSm = ind
        for i in range(ind,len(tlist)):
            if tlist[iSm] > tlist[i]:
                iSm=i
        tlist[ind], tlist[iSm] = tlist[iSm], tlist[ind]
    return tlist

ComputerAssistant4Cards()

'''마술사가 카드를 찾는 방법: 공개되는 카드 중 한장만 Left 이면 그 카드가 기준이 되고 거리는 13보다 작고, 반대로 한장만 Right이면 그 카드가 기준이 되고 거리는 13만큼 떨어지게 된다.\
    그리고 거리가 13이 아닐때 즉 한장만 Left 일 때, 거리를 재는 방식은 교재와 동일하게 공개되는 카드 순서의 크기 배열에 따라 1~6사이의 크기가 된다. 그리고 마지막 힌트로 모든 카드가 Folded Down이면 그 \
    배열에서 얻은 숫자에다가 6을 더해서 최종거리를 구하고, 모든 카드가 shown upward 이면 그냥 배열에 따라 1 ~6 사이의 숫자가 최종 거리가 된다. 그리고 기준카드에서 시계방향으로 거리를 더해서 Hidden 카드 구한다.'''