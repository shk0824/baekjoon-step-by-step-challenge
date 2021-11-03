Talents = ['Sing', 'Dance', 'Magic', 'Act', 'Flex', 'Code']
Candidates = ['Aly', 'Bob', 'Cal', 'Don', 'Eve', 'Fay']
CandidateTalents = [['Flex','Code'], ['Dance', 'Magic'], ['Sing', 'Magic'], ['Sing', 'Dance'], ['Dance', 'Act', 'Code'], ['Act', 'Code']]


def Hire4Show(candList, candTalents, talentsList):
   
    Sol=smallestSol([],candList, candList, candTalents, talentsList,[])    
    print ('Optimum Solution: ', Sol)

def smallestSol(chosen, elts, CandList, CandTal, AllTalents, Sol):
    if len(elts) == 0:
        if Good(chosen, CandList, CandTal, AllTalents):
            if (chosen and Sol==[]) or ( not Sol and (len(chosen)< len(Sol))):
                Sol = chosen
            return Sol
    else:
        if Good(chosen+elts[1:], CandList, CandTal, AllTalents):
            Sol= smallestSol(chosen, elts[1:], CandList, CandTal, AllTalents, Sol)
        return smallestSol(chosen+[elts[0]],elts[1:],CandList, CandTal, AllTalents, Sol)
    
   
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

Hire4Show(Candidates, CandidateTalents, Talents)
#Hire4Show(ShowTalent2,CandidateList2,CandToTalents2)