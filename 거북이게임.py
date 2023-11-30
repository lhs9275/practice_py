import turtle
import random
turtle.setup(width=1024 , height= 768)

turtle.bgcolor("yellow green")

p_1 = turtle.Turtle()
p_1.color("red")
p_1.shape("turtle")
p_1.penup()
p_1.goto(-200,200)

p_2 = turtle.Turtle()
p_2.shape("turtle")
p_2.color("orange")
p_2.penup()
p_2.goto(-200,170)

p_3 = turtle.Turtle()
p_3.shape("turtle")
p_3.color("yellow")
p_3.penup()
p_3.goto(-200,140)

p_4 = turtle.Turtle()
p_4.shape("turtle")
p_4.color("white")
p_4.penup()
p_4.goto(-200,110)

p_5 = turtle.Turtle()
p_5.shape("turtle")
p_5.color("blue")
p_5.penup()
p_5.goto(-200,80)

p_6 = turtle.Turtle()
p_6.shape("turtle")
p_6.color("purple")
p_6.penup()
p_6.goto(-200,50)

p_7 = turtle.Turtle()
p_7.shape("turtle")
p_7.color("brown")
p_7.penup()
p_7.goto(-200,20)

p_8 = turtle.Turtle()
p_8.shape("turtle")
p_8.color("pink")
p_8.penup()
p_8.goto(-200,-10)

p_9 = turtle.Turtle()
p_9.shape("turtle")
p_9.color("tan")
p_9.penup()
p_9.goto(-200,-40)

p_10 = turtle.Turtle()
p_10.shape("turtle")
p_10.color("sky blue")
p_10.penup()
p_10.goto(-200,-70)

dice = [1,2,3,4,5,6]

set1 = -200
set2 = -200 
set3 = -200 
set4 = -200 
set5 = -200 
set6 = -200 
set7 = -200 
set8 = -200 
set9 = -200 
set10 = -200 

s = turtle.Turtle()
s.up()
s.color("black")
s.goto(-180, 300)
s.pendown()
s.pensize(10)
s.goto(-180, -200)
s.penup()
s.goto(320, 300)
s.pendown()
s.pensize(10)
s.goto(320, -200)





while True:

    num = random.choice(dice)
    set1 =  set1 + num*20
    set1 = set1
    p_1.goto(set1, 200)

    if p_1.pos() >= (300,200):
        print("p_1 is winner")
        break
    else:
        num = random.choice(dice)
        set2 =  set2 + num*20
        set2 = set2
        p_2.goto(set2, 170)

        if p_2.pos() >= (300,170):
            print("p_2 is winner")
            break

        else:
            num = random.choice(dice)
            set3 =  set3 + num*20
            set3 = set3
            p_3.goto(set3, 140)
                
            if p_3.pos() >= (300,140):
                print("p_3 is winner")
                break

            else:
                num = random.choice(dice)
                set4 =  set4 + num*20
                set4 = set4
                p_4.goto(set4, 110)

                if p_4.pos() >= (300,110):
                    print("p_4 is winner")
                    break

                else:
                    num = random.choice(dice)
                    set5 =  set5 + num*20
                    set5 = set5
                    p_5.goto(set5, 80)

                    if p_5.pos() >= (300,80):
                        print("p_5 is winner")
                        break

                    else:
                        num = random.choice(dice)
                        set6 =  set6 + num*20
                        set6 = set6
                        p_6.goto(set6, 50)

                        if p_6.pos() >= (300,50):
                            print("p_6 is winner")
                            break

                        else:
                            num = random.choice(dice)
                            set7 =  set7 + num*20
                            set7 = set7
                            p_7.goto(set7, 20)

                            if p_7.pos() >= (300,20):
                                print("p_7 is winner")
                                break

                            else:
                                num = random.choice(dice)
                                set8 =  set8 + num*20
                                set8 = set8
                                p_8.goto(set8, -10)

                                if p_8.pos() >= (300,-10):
                                    print("p_8 is winner")
                                    break

                                else:
                                    num = random.choice(dice)
                                    set9 =  set9 + num*20
                                    set9 = set9
                                    p_9.goto(set9, -40)

                                    if p_9.pos() >= (300,-40):
                                        print("p_9 is winner")
                                        break

                                    else:
                                        num = random.choice(dice)
                                        set10 =  set10 + num*20
                                        set10 = set10
                                        p_10.goto(set10, -70)

                                        if p_10.pos() >= (300,-70):
                                            print("p_10 is winner")
                                            break




    

    


