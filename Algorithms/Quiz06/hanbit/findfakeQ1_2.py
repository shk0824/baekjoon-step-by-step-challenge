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

def findFakeGroupandType(group1, group2, group3):
    result1and2 = compare(group1, group2)
    if result1and2 == 'left':
        result1and3 = compare(group1, group3)
        if result1and3 == 'left':
            fakeGroup = group1
            type = 'heavier'
        elif result1and3 == 'equal':
            type = 'lighter'
            fakeGroup=group2
    elif result1and2 == 'right':
        result3and2 = compare(group3, group2)
        if result3and2 == 'right':
            fakeGroup = group2
            type = 'heavier'
        elif result3and2 == 'equal':
            fakeGroup = group1
            type = 'lighter'
    else:
        result1and3 = compare(group1,group3)
        if result1and3 == "right":
            fakeGroup = group3
            type = 'heavier'
        elif result1and3 == "left":
            fakeGroup = group3
            type = 'lighter'
        else:
            fakeGroup = 'None'
            type = 'same'
    return fakeGroup, type

def findFakeGroupHeavier(group1, group2, group3):
    result1and2 = compare(group1, group2)
    if result1and2 == 'left':
        fakeGroup = group1
    elif result1and2 == 'right':
        fakeGroup = group2
    else:
        fakeGroup = group3
    return fakeGroup




def findFakeGroupLighter(group1, group2, group3):
    result1and2 = compare(group1, group2)
    if result1and2 == 'left':
        fakeGroup = group2
    elif result1and2 == 'right':
        fakeGroup = group1
    else: 
        fakeGroup = group3
    return fakeGroup



def CoinComparisonGeneral(coinsList):
    global counter
    counter = 0
    currList = coinsList
    group1, group2, group3 = splitCoins(currList)
    currList,type = findFakeGroupandType(group1, group2, group3)
    counter += 1
    if currList == 'None':
            print('No Fake Coin')
            print('Number of weighings: ', counter )
            return
    if type =="heavier":
        findFakeGroup=findFakeGroupHeavier
    else: findFakeGroup = findFakeGroupLighter
    while len(currList) > 1:
        group1, group2, group3 = splitCoins(currList)
        currList = findFakeGroup(group1, group2, group3)
        counter += 1
    fake = currList[0]
    print('The fake coin is',type,'and is coin', coinsList.index(fake)+1, 'in the original list')
    print ('Number of weighings: ', counter )



coinsList = [10,10,10,10,10,10,10,10,10,10,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]



CoinComparisonGeneral(coinsList)
