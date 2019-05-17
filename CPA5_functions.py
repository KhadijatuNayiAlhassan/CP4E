''' Author: Khadijatu Nayi Alhassan
CPA5 '''
import math
# Question 3
# def triangle_check(x1,y1,x2,y2,x3,y3):
#     side1 = math.sqrt((x2-x1)**2 + (y2-y1)**2)
#     side2 = math.sqrt((x3-x2)**2 + (y3-y2)**2)
#     side3 = math.sqrt((x3-x1)**2 + (y3-y1)**2)
#     if side1 == side2 or side2 == side3:
#         print('Triangle is isosceles')
#     elif side1 == side2 and side2 == side3:
#         print('Triangle is Equilateral')
#     elif side1 != side2 and side2 != side3:
#         print('Triangle is scalene')
# triangle_check(-3,0,3,0,0,3)

# # Question 1
# list1 = range(1,5)
def pattern(n):
    m = n//2
    for i in range(1,m+2):
        print('*'*i)

    for j in range(-m,0):
        print('*'*abs(j))

# pattern(9)  

for i in range(5):
    for j in range(i+1):
        print('*', end=' ')
    print('\r')

for i in range(4, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print('\r')

# list1 = []
# for j in range(1,5):
#     list1 = list1.append(j)
# list1.reverse()
#     print('*'*i)
# print('*'*list1[j])
# for j in list1:

# print(list1)
# print('*'*i)
# print('*'*)

#Question 3
import random
def guess_game():
    num1 = random.randint(1,9)
    user_guess = int(input('please enter your guess : '))
    while user_guess:
    #user_guess = int(input('please enter your guess : '))
        if user_guess == num1:
            user_guess = False
            print('well done')  
        elif  user_guess != num1:
            user_guess = int(input('please guess again : ')) 
    
