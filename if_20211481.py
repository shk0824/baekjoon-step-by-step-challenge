input_data = input( ).split(' ')
A = int(input_data[0])
B = int(input_data[1])

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')
    



score = int(input())

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
    


    year = int(input( ))

#윤년은 연도가 4의 배수면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
if (year % 4 ==0 and year % 100 !=0) or year % 400 ==0:
    print('1')
else:
    print('0')
    



    x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
        
elif x < 0 and y > 0:
    print(2)
        
elif x < 0 and y < 0:
    print(3)
     
else:
    print(4)
    



    input_data = input().split(' ')

hour = int(input_data[0])
minute = int(input_data[1])

minute -=45
if minute < 0:
    minute +=60
    hour -=1
    if hour <0:
        hour=23
        
print(str(hour)+' '+str(minute))

