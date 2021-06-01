n=int(input())
count=0

def check(x):
    wordlist=[0]
    for i in x:  
        if wordlist[-1]!=i:
            if i in wordlist:
                return False
        wordlist+=[i]

    return True

for i in range(n):
    word=input()
    if check(word):
        count+=1
print(count)

