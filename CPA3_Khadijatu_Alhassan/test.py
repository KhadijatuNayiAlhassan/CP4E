'''Author: Khadijatu Nayi Alhassan
CPA3 
'''
from functions import vol_sphere
from functions import isEven
from functions import pi_approx
from functions import square_root


def main():
    sphere_radius = 5
    print("Volume of sphere with radius " + str(sphere_radius)+ \
        " units is: ", vol_sphere(sphere_radius) , " cubic units ")

    even_or_not = 18
    print(str(even_or_not) + " is even: ", isEven(even_or_not))

    number1 = 50
    n = 10
    print("Square root of " + str(number1) + " = ", square_root(number1,n))

    number2 = 200
    print("PI = ", pi_approx(number2))

main()