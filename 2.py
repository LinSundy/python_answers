# 2.1
# Celsius = input("Enter a degree in Celsius:")
# fahrenheit = (9 / 5) * eval(Celsius) + 32
# print('%s Celsius is %s Fahrenheit' % (Celsius, fahrenheit))


# PI = 3.1415926535
# 2.2
# temp = input("Enter the radius and length of a cylinder:")
# radius, alength = temp.split(',')
# area = eval(radius) ** 2 * PI
# volume = area * eval(alength)
# print('The area is %s' % area)
# print("The volume is %s" % volume)


# 2.3
# feet = eval(input("Enter a value for feet:"))
# meters =  feet * 0.305
# print('%s feet is %s meters' % (feet, meters))


# 2.4
# pounds = eval(input('Enter a value in pounds:'))
# kilograms = pounds * 0.454
# print('%s pounds is %s kilograms' % (pounds, kilograms))


# 2.5
# temp = input('Enter the subtotal and a gratuity rate:')
# subtotal, rate = temp.split(',')
# gratuity = eval(subtotal) * eval(rate) / 100
# total = eval(subtotal) + gratuity
# print('The gratuity is %s and the total is %s' % (gratuity, total))


# 2.6
# num = eval(input('Enter a number between 0 and 1000:'))
# h = num // 100
# t = num // 10 % 10
# n = num % 10
# total = h + t + n
# print('The sum of the digits is %s' % total)


# 2.7
# num = eval(input('Enter the number of minutes:'))
# year = 60 * 24 * 365
# years = num // year
# days = num % year // (60 * 24)
# print('%s minutes is approximately %s years and %s days' % (num, years, days))


# 2.8
# water = eval(input('Enter the amount of water in kilograms:'))
# init_temperature = eval(input('Enter the initial temperature:'))
# final_temperature = eval(input('Enter the final temperature:'))
# Q = water * (final_temperature - init_temperature) * 4184
# print('The energy needed is %s' % Q)


# 2.9
# temperature = eval(input('Enter the temperature in Fahrenheit between -58 and 41:'))
# speed = eval(input('Enter the wind speed in miles per hour:'))
# twc = 35.74 + 0.6215 * temperature - 35.75 * speed**0.16 + 0.4275 * temperature * speed**0.16
# print('The wind chill index is %s' % twc)


# 2.10
# temp = input('Enter speed and acceleration:')
# v,a = temp.split(',')
# l = eval(v)**2 / (2 * eval(a))
# print('The minimum runway length for this airplane is %s meters' % l)


# 2.11
# final_money = eval(input('Enter final account value:'))
# rate = eval(input('Enter annual interest rate in percent:'))
# years = eval(input('Enter number of years:'))
# init_money = final_money / ((1 + rate / 12 / 100) ** (years * 12))
# print('Initial deposit value is %s' % init_money)


# 2.12
# def tables():
#   print('a\tb\ta ** b')
#   for i in range(1, 6):
#     print('%d\t%d\t%d' % (i, i+1, i ** (i+1)))
# tables()


# 2.13
# num = input('Enter an integer:')
# arr = list(num)
# arr.reverse()
# for i in arr:
#   print(i)


# 2.14
# import math
# s = input('Enter thress points for a triangle:')
# x1, y1, x2, y2, x3, y3 = [eval(x) for x in s.split(',')]
# side1 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
# side2 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
# side3 = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
# s = (side1 + side2 + side3) / 2
# area = math.sqrt(s * (s-side1) * (s - side2) * (s - side3))
# print('The area of the triangle is %.1f' % area)


# 2.15
# import math
#
# side = input('Enter the side:')
# area = 3 * math.sqrt(3) / 2 * (eval(side) ** 2)
# print('The area of the hexagon is %.4f' % area)

# 2.17
# pounds = eval(input('Enter weight in pounds:'))
# inches = eval(input('Enter height in inches:'))
# BMI = pounds * 0.45359237 / ((inches * 0.0254) ** 2)
# print('BMI is %.4f' % BMI)
