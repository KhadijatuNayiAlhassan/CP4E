'''Author: Khadijatu Nayi Alhassan
CPA3 '''


import math        
                   
#Question 1
def vol_sphere(r):
    #This function calculates the volume of a sphere
    #given a radius
    pi = math.pi
    volume = 4/3*pi*r**3
    print(str(volume)+" cubic units")
    return volume



#Question 2    
def isEven(number):
    #This function gives an output after checking if a
    #number is even or odd
    if number%2 == 0:
        return True
    else:
        return False


#Question 3
def pi_approx(n):  
    #This function approximates the value of pi by evaluating a sequence
    #with n number of terms in the sequence.
    r = 3
    total = 1  # First term is 1 and the rest accumulates to this value
    for i in range(1,n+1):
        term = (-1)**(i*1)/((2*i+1)*r**i)
        total = total + term # total is updated  each time
    pi = math.sqrt(12)*total
    print(pi)
    return pi

#Question 4
def square_root(num_root,n):
    #This function uses an iteration formula to evaluate
    #the square root of a number.
    x = 1
    for i in range(1, n+1):
        y = 1/2 *(x+ (num_root/x))
        x = y  # after each iteration, the answer serves as the input for the
    print(x)           #next iteration
    return x

#test

def main():
    (vol_sphere(5))
    print(isEven(5))
    pi_approx(200)
    square_root(50,10)
main()
