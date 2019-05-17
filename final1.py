''' 
Author: Khadijatu Nayi Alhassan
Python Project: Probability Calculator
'''
# modules used
import math
from sympy import pi, exp, N, sqrt, oo, Symbol,integrate
from numpy import linspace,zeros,arange
from matplotlib import pyplot as plt

class Probability:
    '''Probability calculator
    '''
    def __init__(self):
        # self.constant = 1/math.sqrt(2*math.pi)
        self.x = Symbol('x')
        # self.z = z
        # self.f_x = math.exp(-((self.x)**2)/2)
       
    def funx(self):
        ''' 
        This function returns the pdf of the normal distribution.
        parameters: none
        returns an expression
        '''
        constant = 1/sqrt(2*pi) 
        f_x = exp(-((self.x)**2)/2)
        pdf = constant*f_x
        return pdf
    
    def normal_dist1(self,mean, sd, x1):
        '''
        this function returns the probability using the normal distribution.
         parameters: 
            mean:the mean of the normal distribution
            sd :the standard deviation of the normal distribution
            x1: a value in the data set of the normal distribution

        returns the calculated probability'''
        z = round(((x1-mean)/sd),3) # round to 3dp
        p = integrate(self.funx(), (self.x, -oo, z)) # integrates the function from negative infinity to z
        prob = {'p(Z<-z)': N(p),'p(Z>-z)':1-N(p)}
        return prob
    
    def plot_norm_dist(self, mean, sd, shade_lt = None, shade_gt = None, shade_bw = None):
        rows = 50
        x = linspace(mean - 3*sd, mean + 3*sd, rows, endpoint = False)
        y = zeros(len(x))


        y_1 = []  #probabilities below the mean.
        y_2 = []  #Probabilities above the mean.


        for i in range(len(y)):
            prob = self.normal_dist1(mean, sd, x[i])
            y_1.append(prob['p(Z<-z)'])
            y_2.append(prob['p(Z>-z)'])

        y_1.extend(y_2) #combine two probabilities to give the full curve

        x_1 = linspace(-5, 5, 2*rows, endpoint = False)  #Form x axis for the combined probabilties
        fig, ax = plt.subplots()  #creates multiple plots on the same graph
        plt.style.use('fivethirtyeight')
        ax.plot(x_1 ,y_1)

        plt.fill_between(x_1 ,y_1)
        # plt.title(title1)
        # plt.fill_between(x_1>condition2,0,y)
        # plt.title(title2)

        plt.show()

    # def sketch(x,condition1,condition2,title1,title2):
       
        
    #     plt.show()

    def normal_dist2(self,mean, sd, x1,x2):
        ''' This function also returns the probability calculated using normal distribution.
            parameters: 
                mean: mean of the normal distribution
                sd: standard deviation of the normal distribution
                x1 and x2: values in the data set of the normal distribution

            returns probability calculated between the values x1 and x2
                '''
        z1 = round(((x1-mean)/sd),3)
        z2 = round(((x2-mean)/sd),3)
        list1 =[z1,z2]
        a = min(list1) # the smallest of the two numbers must always be the lower limit and
        b = max(list1) # the biggest must always be the upper limit of integration
        prob = integrate(self.funx(),(self.x,a,b))
        return {'p(z1<Z<z2)': N(prob)}
        
    def geometric(self, p, x1):
        '''
        This function returns the calculated probability using the geometric distribution.
        parameters: 
            p: probability of success of the geometric distribution
            x1: a value in the data set of the geometric distribution
        returns the probability value 
        ''' 

        p_lt_or_eq = 1-(1-p)**x1
        p_grt_or_eq = (1-p)**(x1-1)
        p_lt = 1-(1-p)**(x1-1)
        p_gt = (1-p)**x1
        E_x = 1/p
        Var_x = 1-p/p**2
        prob = {"Mean E(x)": E_x,"Variance var_x":Var_x,"p(X<=x)":p_lt_or_eq,"p(X>=x)":p_grt_or_eq,"p(X<x)": p_lt,"p(X>x)":p_gt }
        return prob
    
    def exponential(self,L,x1, x2=None):
        ''' This function returns the calculated probability using the exponential distribution.
            parameters:
                L: Average number of events
                x1 and X2 : events duration
        returns the calculated probaility
        '''
        p_limits = None
        p_lt= 1 - math.exp(-L*x1)
        p_gt = math.exp(-L*x1)

        if x2 != None:
            p_limits = math.exp(-L*x2)-math.exp(-L*x1)
        E_x = 1/L
        var_x = 1/L**2
        prob = {"Mean E(x)":E_x,"Variance Var(x)":var_x,"p(X<x)":p_lt,'p(X>x)': p_gt,'p(x1<X<x2)':p_limits}

        return prob

    def poisson(self,L,x1):
        ''' This function returns the calculated probability using the poisson distribution
                parameters:
                    L: Average number of events
                    x1: number of events 
            returns the probability value
            '''
        exactly_x= math.exp(-L)*(L**x1/math.factorial(x1))
        prob1 = 0
        for i in range(0,x1):
            exactly_n1= math.exp(-L)*(L**i/math.factorial(i))
            prob1 = prob1 + exactly_n1

        prob2 = 0    
        for i in range(0,x1+1):
            exactly_n2= math.exp(-L)*(L**i/math.factorial(i))
            prob2 = prob2 + exactly_n2
        prob  = { 'p(X=x)': exactly_x, 'p(X>x)':1-prob2,'At_most_x':prob2,'At_least_x':1-prob1,'p(X<x)':prob1}
        return prob
