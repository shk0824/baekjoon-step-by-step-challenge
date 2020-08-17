def f(n):
    num=sum(int(i)**2 for i in str(n)) #str(n)으로 받아야지 각 자릿수를 분할해서 제곱을 구할 수 있음.
    return num

n=input()
N=int(n)
List=[n] # 한번 싸이클 돌때마다 변하는 수를 포함하는 리스트

while 1:
    n=f(n)
    if n in List: #만약 중복된 숫자가 나오면
        print("UNHAPPY")
        break
    List+=[n] # 중복된게 아니면 리스트에 넣기
    if n==1: #1이랑 같으면 happy!
        print ("HAPPY")
        break
