from CPA5 import *
def main():
    print('Question 1')
    print('-------------------------------------------------')
    rows = int(input('Please input an odd number of rows: '))
    draw_pattern(rows)
    print()

    print('Question 2')
    print('-------------------------------------------------')
    guess_game()
    print()

    print('Question 3')
    print('-------------------------------------------------')
    triangle = triangle_check(-3,0,3,0,0,3)#isosceles
    triangle1 = triangle_check(9,15,20,5,20,13)#scalene
    print(triangle)
    print(triangle1)
    print()     
    
    print('Question 4')
    print('-------------------------------------------------')
    rows = int(input('Please input number of rows: '))
    pascal(rows)
    print()

main()