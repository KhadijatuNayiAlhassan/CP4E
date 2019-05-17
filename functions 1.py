''' Author: Khadijatu Nayi Alhassan
CPA2  '''

def sum_even():
     sum_k = 0
     for k in range(2,202,2):
         sum_k = sum_k + k
     print(sum_k)
         
    


def sum_odd():
    sum_p = 0
    for p in range(1,100,2):
        sum_p = sum_p + p
    print(sum_p)
    
 


def fib(N):     #this function prints the nth fibonacci number
     if N == 1:
          return 1
     elif N == 2:  #the first and the second terms are 1 and 1
          return 1
     else:
          n = fib(N - 1) + fib(N - 2) # any term n >= 3 can be found with
                                        #this formula
     return n
     






def wallis(n):    #this function writes the 2nd to the nth wallis term
     ans = '2*2/1' 
     for i in range(1, n+1):   
          a = 2*i
          b = 2*i+1   # derived formula for each term
          c = 2*i+2
          ans = ans + '*' + (str(a) +"/" +str(b) +"*" + str(c) +"/" + str(b))
     
     print(ans)



def factorial(n):
     
     number = 1 #the last term in the factorial is 1
     for i in range(1,n+1):
          number = number*i  #number is updated each time
     print(number)



#test
def main():
     sum_even()
     sum_odd()
     fib(8)
     wallis(5)
     print('\n')
     factorial(5)

main()

     
