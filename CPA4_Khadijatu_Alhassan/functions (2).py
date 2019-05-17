'''Author: Khadijatu Nayi Alhassan
CPA3 '''


import math        #this function calculates the volume of a sphere
                   #given a radius
def vol_sphere(r):
    pi = math.pi
    volume = 4/3*pi*r**3
    print(str(volume) + " cubic units ")
    return(volume)



    
def isEven(number):    # this function gives an output after checking if a
                       #number is even or odd
    if number%2 == 0:
        print (True)
    else:
        print (False)




def iteration(num_root,n):  #this function uses an iteration formulato evaluate
                           #the square root of a number
    x = 1
    for i in range(1,n+1):
        y = 1/2*(x+num_root/x)
        x = y  # after each iteration, the answer serves as the input for the
               #next iteration
    print(x)


import math     #this function approximates the value of pi by evaluating a
                #sequence
def pi_approx(n):  # n is the number of terms i want in the sequence
              
    r = 3
    total = 1  # first term is 1 and the rest accumulates to this value
    for i in range(1,n+1):
        term = (-1)**i*1/((2*i+1)*r**i)
        total = total + term # total is updated  each time
    pi = math.sqrt(12)*total
    print(pi)


def main():
    vol_sphere(5)
    isEven(18)
    isEven(5)
    iteration(50,10)
    pi_approx(200)

main()
