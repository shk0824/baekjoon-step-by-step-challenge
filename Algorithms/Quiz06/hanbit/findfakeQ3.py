def compare(groupA, groupB):
    if sum(groupA)>sum(groupB):
        result='left'
    elif sum(groupB)>sum(groupA):
        result='right'
    else: result = 'equal'
    return result

def splitCoins(coinslist):
    length = len(coinslist)
    group1 = coinslist[0:length//3]
    group2 = coinslist[length//3:length//3*2]
    group3 = coinslist[length//3*2:length]
    return group1, group2, group3


def findFakeGroupandType2(group1, group2, group3):
    global counter
    result1and2 = compare(group1, group2)
    if result1and2 == 'left':
        fakeGroup = group1
    elif result1and2 == 'right':
        fakeGroup = group2
    else:
        counter+=1
        result1and3 = compare(group1,group3)
        if result1and3 == "right":
            fakeGroup = group3
        elif result1and3 == "left":
            fakeGroup = group1
        else:
            fakeGroup = 'None'
            type = 'same'
    type= 'heavier'
    return fakeGroup, type

def findFakeGroupHeavier2(group1, group2, group3):
    global counter
    result1and2 = compare(group1, group2)
    if result1and2 == 'left':
        fakeGroup = group1
    elif result1and2 == 'right':
        fakeGroup = group2
    else:
        result1and3 =compare(group1,group3)
        counter+=1
        if result1and3 != 'left':
            fakeGroup = group3
        else: fakeGroup = group1
    return fakeGroup


def CoinComparisonGeneral(coinsList):
    global counter
    counter = 0
    currList = coinsList
    group1, group2, group3 = splitCoins(currList)
    currList,type = findFakeGroupandType2(group1, group2, group3)
    counter += 1
    if currList == 'None':
            print('No Fake Coin')
            print('Number of weighings: ', counter )
            return
    findFakeGroup=findFakeGroupHeavier2
    while len(currList) > 1:
        group1, group2, group3 = splitCoins(currList)
        currList = findFakeGroup(group1, group2, group3)
        counter += 1
    fake = currList[0]
    print('The fake coin is coin', coinsList.index(fake)+1, 'in the original list')
    print ('Number of weighings: ', counter )



coinsList = [10,10,10,10,10,10,10,10,10,10,12,10,10,10,10,10,10,10,10,10,10,10,12,10,10,10,10]


CoinComparisonGeneral(coinsList)

