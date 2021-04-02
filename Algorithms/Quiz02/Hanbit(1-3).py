sched=[(6,8),(6,12),(6,7),(7,8),(7,10), \
(10,11),(11,12),(7,11),(6,8),(6,8),(7,8), \
(8,10),(8,11),(8,10),(8,12),(11,12),(10,12),(11,12),(7,11)]

def celebrityDensity(sched,start,end):
    count=[0]*(end+1)
    for i in range(start,end+1):
        count[i]=0
        for c in sched:
            if c[0]<=i and c[1]>i:
                count[i]+=1
    return count

def bestTimeToParty (schedule):
    start=schedule[0][0]
    end=schedule[0][1]
    for c in schedule:
        start=min(c[0],start)
        end=max(c[1],end)
    count=celebrityDensity(schedule,start,end)
    maxcount=0
    for i in range(start,end+1):
        if count[i]>maxcount:
            maxcount=count[i]
            time=i
    print('Best time to attend the party is at', time, 'o\clock', ':', maxcount, 'celebrities will be attending!')


#bestTimeToParty(sched)

sched2=[(6.0,8.0),(6.0,12.0),(6.0,7.0),(7.0,8.0),(7.0,10.0), \
(10.0,11.0),(11.0,12.0),(7.0,11.0),(6.0,8.0),(6.0,8.0),(7.0,8.0), \
(8.0,10.0),(8.0,11.0),(8.0,10.0),(8.0,12.0),(11.0,12.0),(10.0,12.0),(11.0,12.0),(7.0,11.0)]

def sortlist(times):
    for ind in range(len(times)-1):
        iSm=ind
        for i in range(ind,len(times)):
            if times[iSm][0]>times[i][0]:
                iSm=i
        times[ind],times[iSm]=times[iSm],times[ind]
    return times
    
def chooseTime(sched):
    count=0
    max=0
    times=0
    for c in sched:
        if c[1]=="start":
            count+=1
        else:
            count-=1
        if max<count:
            max=count
            times=c[0]
    return max,times

def bestTimeToPartySmart(schedule):
    times=[]
    for c in schedule:
        times.append((c[0],'start'))
        times.append((c[1],'end'))
    sched=sortlist(times)
    max,time=chooseTime(sched)
    print('Best time to attend the party is at', time , 'o\clock', ':', max, 'celebrities will be attending!')

#bestTimeToPartySmart(sched2)

sched3=[(6.0,8.0,2),(6.5,12.0,1),(6.5,7.0,2),(7.0,8.0,2),
(7.5,10.0,3),(8.0,9.0,2),(8.0,10.0,1),(9.0,12.0,2),(9.5,10.0,4),
(10.0,11.0,2),(10.0,12.0,3),(11.0,12.0,7)]


def chooseTimewithScore(sched,score):
    max_score=0
    final_count=0
    times=0
    count=0
    total=0
    for c in sched:
        if c[1]=="start":
            total+=score[c[2]]
            count+=1
        else:
            total-=score[c[2]]
            count-=1
        if max_score<total:
            max_score=total
            times=c[0]
            final_count=count
    return max_score,times,final_count

def bestTimeToPartySmartwithScore(schedule):
    times=[]
    score=[]
    for i,c in enumerate(schedule):
        times.append((c[0],'start',i))
        times.append((c[1],'end',i))
        score+=[c[2]]
    sched=sortlist(times)
    max,time,count=chooseTimewithScore(sched,score)
    print('Best time to attend the party is at', time , 'o\clock', ':', count, 
        'celebrities will be attending! and you can enjoy total likeness of',max,"!")


bestTimeToPartySmartwithScore(sched3)
