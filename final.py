''' 
Author: Khadijatu Nayi Alhassan
Python Project: Probability Calculator
'''
# modules used
import math
from sympy import pi, exp, N, sqrt, oo, Symbol,integrate
from matplotlib import pyplot as plt
import numpy as np 

class Probability:
    '''Probability calculator
    '''
    def __init__(self):
        self.x = Symbol('x')

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
        prob = {'p(Z<-z)': N(p),'p(Z>-z)':1-N(p)} # total area under the curve is 1
        return prob
    
    def plot_norm_dist(self, mean, sd, shade_lt = None, shade_gt = None, shade_bw = None,):
        ''' This function draws a normal didtribution  curve and shades a region as 
        specified by the user.
        parameters: 
        mean and sd: characteristics of the normal distribution
        shade_lt: plots a graph to shade all values less than or equal to the z-value
        shade-gt: plots a graph to shade all values greater than or equal to the z-value
        shade_bw: plots a graph to shade between two z-values
        returns a graphical representation of the plot'''
        
        rows = 50
        x = np.linspace(-5, 5, rows, endpoint = False)# produces all values on the x-axis
        y = np.zeros(len(x))

        y_1 = []  #probabilities below the mean.
        y_2 = []  #Probabilities above the mean.
        for i in range(len(y)):
            prob = self.normal_dist1(0, 1, x[i])
            y_1.append(prob['p(Z<-z)'])
            y_2.append(prob['p(Z>-z)'])

        y_1.extend(y_2) #combine two probabilities to give the full curve

        x_1 = np.linspace(-5, 5, 2*rows, endpoint = False)  #Form x axis for the combined probabilties

        fig, graph = plt.subplots(figsize=(9,6)) #subplots allows us to create multiple plots on the same graph
        y_1 = np.array(y_1).astype(np.float64) 
        plt.style.use('fivethirtyeight') 
        graph.plot(x_1,y_1)
        graph.fill_between(x_1, y_1, 0, alpha=0.1)

        if shade_lt:
            z = round(((shade_lt-mean)/sd),3)
            x_lt = [] 
            y_lt = []
            for i in range(len(x_1)):
                if x_1[i] <= z: # develop all pairs of x and y points <= the z-value
                    x_lt.append(x_1[i])
                    y_lt.append(y_1[i])
            
            x_lt = np.array(x_lt).astype(np.float64) # converts the list to a numpy array
            y_lt = np.array(y_lt).astype(np.float64)

            graph.fill_between(x_lt, y_lt, 0, color='g', alpha=0.8)
    # the alpha allows us to see the different colours in the plot more distinctly

        elif shade_gt:
            z = round(((shade_gt-mean)/sd),3)
            x_gt = [] 
            y_gt = []
            for i in range(len(x_1)):
                if x_1[i] >= z:
                    x_gt.append(x_1[i])
                    y_gt.append(y_1[i])
            
            x_gt = np.array(x_gt).astype(np.float64)# convert the lists to a numpy array and the entities from objects to float
            y_gt = np.array(y_gt).astype(np.float64)

            graph.fill_between(x_gt, y_gt, 0, color='r', alpha=0.3)

        elif shade_bw:
            x1 = eval(shade_bw.split(',')[0])
            x2 = eval(shade_bw.split(',')[1])

            z1 = round(((x1-mean)/sd),3)
            z2 = round(((x2-mean)/sd),3)
        

            x_bt = [] 
            y_bt = []
            for i in range(len(x_1)):
                if  z1 <= x_1[i] <= z2: # for all values on the x-axis between z1 and z2,
                    x_bt.append(x_1[i])# append to x_bt, and their corresponding y-values to y_bt
                    y_bt.append(y_1[i])
            
            x_bt = np.array(x_bt).astype(np.float64)
            y_bt = np.array(y_bt).astype(np.float64)
            graph.fill_between(x_bt, y_bt, 0, color='r', alpha=0.3) # this shades the region between x_bt and y_bt

        plt.show()

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
        Var_x = (1-p)/p**2
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
        var_x = 1/(L**2)
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
        prob  = { 'p(X=x)': exactly_x, 'p(X>x)':1-prob2,'At_most_x':prob2,'At_least_x':1-prob1,'p(X<x)':prob1,
                   'mean E(x)': L, 'Variance Var(x)':L }
        return prob