cap1=['F','F','B','B','B','F','B','B','B','F','F','B','F','B','F','B','B']
cap2=['F','B','B','B','B','B','F','B','B','B',' ',' ','F','F','B','F','F','F','F','F',"B","F"]


#1 
def pleaseConform(caps):
    start=forward=backward=0
    caps=caps+['E']
    interval=[]
    for i in range(1,len(caps)):
        if caps[i]=='E':
            continue
        if caps[start] !=caps[i]:
            if caps[start]=="F":
                forward+=1
            else:
                backward+=1
            interval+=[(start,i-1,caps[start])]
            start=i
    if forward>backward:
        flip="B"
    else:
        flip="F"
    for t in interval:
        if t[2]== flip:
            if t[0]==t[1]:
                print("People in postions",t[0], "flip your caps!")
            else:
                print('People in positions', t[0],
                'through',t[1], "flip your caps!")  

#pleaseConform(cap1)



#2
def pleaseConformOnepass(caps):
    caps=caps+[caps[0]]
    empty=0
    for i in range(1, len(caps)):
        if caps[i]==" ":
            empty+=1
        if caps[i]!=caps[i-1] and caps[i] != " ":
            if caps[i]!=caps[0]:
                print("People in postions", i-empty, end = " ")
            else:
                if caps[i-2]==caps[i]:
                    print("flip your caps!")
                else:
                    print("through", i-1-empty, "flip your caps!")

#pleaseConformOnepass(cap2)
#pleaseConformOnepass(cap1)

#3
def pleaseConformWithoutHat(caps):
    start=forward=backward=NoHat=0
    caps=caps+['E']
    interval=[]
    for i in range(1,len(caps)):
        if caps[start] !=caps[i]:
            if caps[start]=="F":
                forward+=1
            if caps[start]=='H':
                NoHat+=1
            if caps[start]=='B':
                backward+=1
            interval+=[(start,i-1,caps[start])]
            start=i
    print(forward,backward)
    if forward>backward:
        flip="B"
    else:
        flip="F"
    for t in interval:
        if t[2]== flip:
            if t[0]==t[1]:
                print("People in postions",t[0], "flip your caps!")
            else:
                print('People in positions', t[0],
                'through',t[1], "flip your caps!")

cap3=['F','F','B','H','B','F','B','B','B','F','H','F','F']
#pleaseConformWithoutHat(cap3)
