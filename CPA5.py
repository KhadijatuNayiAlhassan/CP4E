''' Author: Khadijatu Nayi Alhassan
CPA5 '''
import math
import random

#Question 1 
''' This function draws a pattern.
parameters: rows = total number of rows in the pattern. Rows should be odd.
prints a pattern'''
def draw_pattern(rows):
    for i in range((rows//2)+1):
        for j in range(i+1):
            print('*', end=' ')
        print('\r')

    for i in range(rows//2, 0, -1):
        for j in range(i):
            print('*', end=' ')
        print('\r')


#Question 2
'''This function generates a random number and asks the user to guess that number.
Once the user gets it correct, the code quits.
parameters: it takes no parameters
it does not return any value'''

def guess_game():
    num1 = random.randint(1,9)
    user_guess = int(input('please enter your guess : '))
    while user_guess:
        if user_guess == num1:
            user_guess = False
            print('well guessed')  
        elif  user_guess != num1:
            user_guess = int(input('please guess again : ')) 

#Question 3
''' This function checks if a triangle is equilateral, scalene or isosceles.
parameters: the coordinates of the vertices of the triangle
prints a string '''
def triangle_check(x1,y1,x2,y2,x3,y3):
    side1 = math.sqrt((x2-x1)**2 + (y2-y1)**2) # calculates the distance between two points
    side2 = math.sqrt((x3-x2)**2 + (y3-y2)**2)
    side3 = math.sqrt((x3-x1)**2 + (y3-y1)**2)
    if side1 == side2 and side2 == side3 and side1 == side3: 
        triangle = 'Triangle is equilateral'
    elif side1 == side2 or  side2 == side3 or side1 == side3:
        triangle = 'Triangle is isosceles'
    elif side1 != side2 and side2 != side3:
        triangle = 'Triangle is scalene'
    
    return triangle

#Question 4#
''' This function prints the pascal triangle. The first nested loop calculates the entries of the triangle
in a list. The second nested list arranges the entries in a triangle-like array.
parameters: n = number of rows of the pascal triangle
returns a pattern of numbers of the pascal triangle'''

def pascal(n):
    pascal_rows = []
    for row in range(n+1):
        rows = []
        for r in range(row+1):
            nCr = math.factorial(row)//(math.factorial(row-r)*math.factorial(r))# the formula for n combination r
            rows.append(nCr)
        pascal_rows.append(rows)

    for i in range(n+1):
        print(' '*(n-i), end= ' ')
        for j in range(i+1):
            print(pascal_rows[i][j], end=' ')# end=' ' keeps the content of each iteration in the same line
        print('\r')#removes the space between successive rows 
