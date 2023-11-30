from random import randint

q= 0
Q=0
a_1 = 1 
b_1 = 1 
c_1 = 1 
ball_count = 0
strike_count = 0
out_count = 0
white_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9" ] #함수 비교를 위한 리스트 
num_lit  = [a_1 ,b_1 , c_1]

answer_list = []                          
i = 0     
new_number = 0
while i < 3:  
    new_number = randint(1, 9)       
    if new_number not in answer_list :     
        answer_list.append(new_number)    
        i += 1
print("1과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다")


a =answer_list[0]  
b =answer_list[1]
c =answer_list[2]
a_1 = 1 
b_1 = 1 
c_1 = 1


while (num_lit) != answer_list:

    try:
        print("3자리 자연수를 하나씩 입력하세요 ")
        a_1 =  (input("백의 자리 =" ))
        if   a_1 == 'q':
            break
        if   a_1 == 'Q':
        
            break

        if a_1 == white_list[0]:      # 100의자리
             a_1 = int(a_1)
        elif a_1 == white_list[1]:
             a_1 = int(a_1)
        elif a_1 == white_list[2]:
             a_1 = int(a_1)   
        elif a_1 == white_list[3]:
             a_1 = int(a_1)
        elif a_1 == white_list[4]:
             a_1 = int(a_1)
        elif a_1 == white_list[5]:
             a_1 = int(a_1)
        elif a_1 == white_list[6]:
             a_1 = int(a_1)
        elif a_1 == white_list[7]:
             a_1 = int(a_1)
        elif a_1 == white_list[8]:
             a_1 = int(a_1)
        
        else:
            while(type(a_1) is not int):
                try:
                    a_1 = int(input("정수를 입력해주세요"))
                except:
                    continue 

        

        b_1 =  (input("십의자리 ="))       # 심의자리 
        if   b_1 == 'q':
            break
        if   b_1 == 'Q':
            break

        if b_1 == white_list[0]:
             b_1 = int(b_1)
        elif b_1 == white_list[1]:
             b_1 = int(b_1)
        elif b_1 == white_list[2]:
             b_1 = int(b_1)   
        elif b_1 == white_list[3]:
             b_1 = int(b_1)
        elif b_1 == white_list[4]:
             b_1 = int(b_1)
        elif b_1 == white_list[5]:
             b_1 = int(b_1)
        elif b_1 == white_list[6]:
             b_1 = int(b_1)
        elif b_1 == white_list[7]:
             b_1 = int(b_1)
        elif b_1 == white_list[8]:
             b_1 = int(b_1)
           
        while(type(b_1) is not int):
            try:
                b_1 = int(input("정수를 입력해주세요"))
            except:
                continue 

        c_1 =  (input("일의자리 ="))         # 일의자리
        if   c_1 == 'q':
            break
        if   c_1 == 'Q':
            break

        if c_1 == white_list[0]:
             c_1 = int(c_1)
        elif c_1 == white_list[1]:
             c_1 = int(c_1)
        elif c_1 == white_list[2]:
             c_1 = int(c_1)   
        elif c_1 == white_list[3]:
             c_1 = int(c_1)
        elif c_1 == white_list[4]:
             c_1 = int(c_1)
        elif c_1 == white_list[5]:
             c_1 = int(c_1)
        elif c_1 == white_list[6]:
             c_1 = int(c_1)
        elif c_1 == white_list[7]:
             c_1 = int(c_1)
        elif c_1 == white_list[8]:
             c_1 = int(c_1)

        while(type(c_1) is not int):
            try:
                c_1 = int(input("정수를 입력해주세요"))
            except:
                continue 

        num_lit  = [a_1 ,b_1 , c_1]    # 비교가능하게 class 변경 
        answer_list = [a,b,c]

    except:                            # 되돌리기 
        continue

    if num_lit[0] == answer_list[0]:  # 대조 
        strike_count = strike_count +1 

    elif num_lit[0] == answer_list[1]:
        ball_count = ball_count +1 

    elif num_lit[0] == answer_list [2]:

        ball_count = ball_count +1 

    elif num_lit[0] != answer_list[0:2]:

        out_count = out_count +1


    if int(num_lit[1]) == int(answer_list[0]):  
          ball_count = ball_count +1 
    elif int(num_lit[1]) == int(answer_list[1]): 
        strike_count = strike_count +1
    elif int(num_lit[1]) == int(answer_list[2]):
        ball_count = ball_count +1 
    elif num_lit[1] != answer_list[0:2]:
        out_count = out_count +1
    if  int(num_lit[2]) == int(answer_list[0]):
        ball_count = ball_count +1
    elif int(num_lit[2]) == int(answer_list[1]):

        ball_count = ball_count +1

    elif int(num_lit[2]) == int(answer_list[2]):
    
        strike_count = strike_count +1

    elif  num_lit[2] != answer_list[0:2]:

        out_count = out_count +1 

    if strike_count ==3:      # 정답 호출  
        print("정답입니다 ")
    
    elif strike_count <3:
        print(out_count,"out")
        print(strike_count,"strike")
        print(ball_count,"ball")

    ball_count = 0
    strike_count = 0
    out_count = 0
    
print("게임 끝")






