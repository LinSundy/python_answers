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
def pi(num):
    step = 0
    total = 0
    for i in range(1, num, 2):
        if step % 2 != 0 :
           total += - (1 / i)
        else:
            total += (1 / i)
        step += 1
    return 4 * total
# print(pi(1000000))
# print(pi(16))

# 1.8
Pi = pi(100000)
def showInfo(r):
    print(r**2 * Pi, '圆的面积')
    print(2 * r * Pi, "圆的周长")
showInfo(5.5)