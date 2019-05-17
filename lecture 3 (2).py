##import turtle
##a= turtle.Turtle()
####for i in range(4):
####	a.forward(100)
####	a.right(90)
##
##for j in range(3):
##    a.left(120)
##    a.forward(100)
##	


##import math
##print(math.pi)
def vol(bA,h):
     # this code calculates the volume of a cylinder
     v = bA*h
     return v
def bA(r):
    import math
    pi = math.pi
    p = pi*r**2
    return p
def main():
    r = 2
    h = 4
    p = bA(r)
    v = vol(p,h)
    print(v)
