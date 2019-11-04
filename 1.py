# 1.1
# print("Welcome to Python")
# print("Welcome to Computer Science")
# print("Programming is fun")

# 1.2
# print("Welcome to Python\t" * 5)

# 1.3
# print("F"*7 + " " * 4 + "U" + " " * 5 + "U" + " " * 4 + "NN" + " " * 5 + "NN")
# print("FF" + " " * 9 + "U" + " " * 5 + "U" + " " * 4 + "NNN" + " " * 4 + "NN")
# print("F"*7 + " " * 4 + "U" + " " * 5 + "U" + " " * 4 + "NN" + " " + "N" + " " * 3 + "NN")
# print("FF" + " " * 10 + "U" + " " * 3 + "U" + " " * 5 + "NN" + " " * 2 + "N" + " " * 2 + "NN")
# print("FF" + " " * 11 + "UUU" + " " * 6 + "NN" + " " * 4 + "N" * 3)

# 1.4
# arr = [1, 2, 3, 4]
# print("a\t\t" + "a^2\t\t" + "a^3")
# for i in arr:
#     print(i, end="\t\t")
#     print(i**2, end="\t\t")
#     print(i**3)

# 1.5
# print((9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5))

# 1.6
# total = 0
# for i in range(1, 10):
#     total += i
# print(total)

# 1.7
# def pi(num):
#     step = 0
#     total = 0
#     for i in range(1, num, 2):
#         if step % 2 != 0 :
#            total += - (1 / i)
#         else:
#             total += (1 / i)
#         step += 1
#     return 4 * total
# print(pi(1000000))
# print(pi(16))

# 1.8
# Pi = pi(100000)
# def showInfo(r):
#     print(r**2 * Pi, '圆的面积')
#     print(2 * r * Pi, "圆的周长")
# showInfo(5.5)

# 1.9
# def rectangle(w, h):
#     print(w * h, "矩形的面积")
#     print(2 * (w + h), "矩形的周长")
# rectangle(4.5, 7.9)

# 1.10
# def aveSpeed():
#     time = 45 * 60 + 30
#     li =  14
#     _speed = li / time
#     return _speed * 3600 / 1.6
# print(aveSpeed(), '平均速度/英里')

# 1.11
# def peopleNum():
#     currentPeople = 3120324986
#     time = 365 * 24 * 60 * 60
#     for i in range(1, 6):
#         currentPeople += time // 7
#         currentPeople -= time // 13
#         currentPeople -= time // 45
#         print('第%d年的总人数是%d' % (i, currentPeople))
# peopleNum()

# 1.12
# def zhengfangxing():
#     turtle.showturtle()
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(200)
#     turtle.right(90)
#     turtle.forward(200)
#     turtle.right(90)
#     turtle.forward(200)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.penup()
#     turtle.goto(-100, 0)
#     turtle.pendown()
#     turtle.right(180)
#     turtle.forward(200)
#     turtle.penup()
#     turtle.goto(0, 100)
#     turtle.pendown()
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.done()
# zhengfangxing()

# 1.13
# def shizi():
#     turtle.showturtle()
#     turtle.penup()
#     turtle.goto(-100, 0)
#     turtle.pendown()
#     turtle.forward(200)
#     turtle.penup()
#     turtle.goto(0, 100)
#     turtle.right(90)
#     turtle.pendown()
#     turtle.forward(200)
#     turtle.done()
# shizi()

import turtle
t = turtle.Turtle()
# 1.14
# def sanjiao():
#     turtle.showturtle()
#     turtle.right(60)
#     turtle.forward(100)
#     turtle.right(120)
#     turtle.forward(100)
#     turtle.right(120)
#     turtle.forward(100)
#     turtle.done()
# sanjiao()

# 1.15
# def twoSanjiao():
#     turtle.showturtle()
#     turtle.right(60)
#     turtle.forward(100)
#     turtle.right(120)
#     turtle.forward(100)
#     turtle.right(120)
#     turtle.forward(200)
#     turtle.right(240)
#     turtle.forward(100)
#     turtle.right(240)
#     turtle.forward(100)
#     turtle.done()
# twoSanjiao()

# 1.16
# def circle():
#     turtle.showturtle()
#     turtle.penup()
#     turtle.goto(-50, 50)
#     turtle.pendown()
#     turtle.circle(50)
#     turtle.penup()
#     turtle.goto(50, 50)
#     turtle.pendown()
#     turtle.circle(50)
#     turtle.penup()
#     turtle.goto(50, -50)
#     turtle.pendown()
#     turtle.circle(50)
#     turtle.penup()
#     turtle.goto(-50, -50)
#     turtle.pendown()
#     turtle.circle(50)
#     turtle.done()
# circle()

# 1.17
# def zhixian():
#     t.showturtle()
#     t.penup()
#     t.goto(-39, 48)
#     t.write('(-39, 48)')
#     t.color('red')
#     t.pendown()
#     t.goto(50, -50)
#     t.color('black')
#     t.write('(50, -50)')
#     turtle.done()
# zhixian()

# 1.18
# def star():
#     import turtle
#     turtle.showturtle()
#     turtle.penup()
#     turtle.goto(0, 100)
#     turtle.pendown()
#     turtle.right(72)
#     turtle.forward(300)
#     turtle.right(144)
#     turtle.forward(300)
#     turtle.right(144)
#     turtle.forward(300)
#     turtle.right(144)
#     turtle.forward(300)
#     turtle.right(144)
#     turtle.forward(300)
#     turtle.done()
# star()


# 1.19
# def duobianxing():
#     t.showturtle()
#     t.penup()
#     t.goto(40, -69.28)
#     t.pendown()
#     t.goto(-40, -69.28)
#     t.goto(-80, -9.8)
#     t.goto(-40, 69)
#     t.goto(40, 69)
#     t.goto(80, 0)
#     t.goto(40, -69.28)
#     turtle.done()
# duobianxing()


# 1.20
# def lifangti():
#   t.showturtle()
#   t.penup()
#   t.goto(-100, 50)
#   t.pendown()
#   t.goto(100, 50)
#   t.goto(60, 10)
#   t.goto(-140, 10)
#   t.goto(-100, 50)


#   t.penup()
#   t.goto(-100, -50)
#   t.pendown()
#   t.goto(100, -50)
#   t.goto(60, -90)
#   t.goto(-140, -90)
#   t.goto(-100, -50)

#   t.penup()
#   t.goto(100, 50)
#   t.pendown()
#   t.goto(100, -50)

#   t.penup()
#   t.goto(-100, 50)
#   t.pendown()
#   t.goto(-100, -50)

#   t.penup()
#   t.goto(60, 10)
#   t.pendown()
#   t.goto(60, -90)

#   t.penup()
#   t.goto(-140, 10)
#   t.pendown()
#   t.goto(-140, -90)
#   turtle.done()
# lifangti()
