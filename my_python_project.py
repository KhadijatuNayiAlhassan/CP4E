''' Author: Khadijatu Nayi Alhassan
Python Project '''

'''this function returns the probability reading from the table. the number of decimal places of the z_value.
parameters: zval
returns the value of the probability.'''
import math
def phi(zval): 
        
        z_score = {
          0.0 : {'2dp':{0:0.5000, 1:0.5040, 2:0.5080, 3:0.5120, 4:0.5160, 5:0.5199, 6:0.5239, 7:0.5279, 8:0.5319, 9:0.5359}, '3dp':{1:4, 2:8, 3:12, 4:16, 5:20, 6:24, 7:28, 8:32, 9:36}},
          0.2 : {'2dp':{0:0.5793, 1:0.5832, 2:0.5871, 3:0.5910, 4:0.5948, 5:0.5987, 6:0.6026, 7:0.6064, 8:0.6103, 9:0.6141},'3dp':{1:4, 2:8, 3:12, 4:15, 5:19, 6:23, 7:27, 8:31, 9:35}},                        
          0.3 : {'2dp':{0:0.6179, 1:0.6217, 2:0.6255, 3:0.6293, 4:0.6331, 5:0.6368, 6:0.6406, 7:0.6443, 8:0.6480, 9:0.6517},'3dp':{1:4, 2:7, 3:11, 4:15, 5:19, 6:22, 7:26, 8:30, 9:34}},                        
          0.4 : {'2dp':{0:0.6554, 1:0.6591, 2:0.6628, 3:0.6664, 4:0.6700, 5:0.6736, 6:0.6772, 7:0.6808, 8:0.6844, 9:0.6879},'3dp':{1:4, 2:7, 3:11, 4:14, 5:18, 6:22, 7:25, 8:29, 9:32}},                         
          0.5 : {'2dp':{0:0.6915, 1:0.6950, 2:0.6985, 3:0.7019, 4:0.7054, 5:0.7088, 6:0.7123, 7:0.7157, 8:0.7190, 9:0.7224},'3dp':{1:3, 2:7, 3:10, 4:14, 5:17, 6:20, 7:24, 8:27, 9:31}},                             
          0.6 : {'2dp':{0:0.7257, 1:0.7291, 2:0.7324, 3:0.7357, 4:0.7389, 5:0.7422, 6:0.7454, 7:0.7486, 8:0.7517, 9:0.7549},'3dp':{1:3, 2:7, 3:10, 4:13, 5:16, 6:19, 7:23, 8:26, 9:29}},                             
          0.7 : {'2dp':{0:0.7580, 1:0.7611, 2:0.7642, 3:0.7673, 4:0.7704, 5:0.7734, 6:0.7764, 7:0.7794, 8:0.7823, 9:0.7852},'3dp':{1:3, 2:6, 3:9, 4:12, 5:15, 6:18, 7:21, 8:24, 9:27}},
          0.8 : {'2dp':{0:0.7881, 1:0.7910, 2:0.7939, 3:0.7967, 4:0.7995, 5:0.8023, 6:0.8051, 7:0.8078, 8:0.8106, 9:0.8133},'3dp':{1:3, 2:5, 3:8, 4:11, 5:14, 6:16, 7:19, 8:22, 9:25}},
          0.9 : {'3dp':{0:0.8159, 1:0.8186, 2:0.8212, 3:0.8238, 4:0.8264, 5:0.8289, 6:0.8315, 7:0.8340, 8:0.8365, 9:0.8389},'3dp':{1:3, 2:5, 3:8, 4:10, 5:13, 6:15, 7:18, 8:20, 9:23}},
          1.0 : {'2dp':{0:0.8413, 1:0.8438, 2:0.8461, 3:0.8485, 4:0.8508, 5:0.8531, 6:0.8554, 7:0.8577, 8:0.8599, 9:0.8621},'3dp':{1:2, 2:5, 3:7, 4:9, 5:12, 6:14, 7:16, 8:19, 9:21}},
          1.1 : {'2dp':{0:0.8643, 1:0.8665, 2:0.8686, 3:0.8708, 4:0.8729, 5:0.8749, 6:0.8770, 7:0.8790, 8:0.8810, 9:0.8830},'3dp':{1:2, 2:4, 3:6, 4:8, 5:10, 6:12, 7:14, 8:16, 9:18}},
          1.2 : {'2dp':{0:0.8849, 1:0.8869, 2:0.8888, 3:0.8907, 4:0.8925, 5:0.8944, 6:0.8962, 7:0.8980, 8:0.8997, 9:0.9015},'3dp':{1:2, 2:4, 3:6, 4:7, 5:9, 6:11, 7:13, 8:15, 9:17}},        
          1.4 : {'2dp':{0:0.9192, 1:0.9207, 2:0.9222, 3:0.9236, 4:0.9251, 5:0.9265, 6:0.9279, 7:0.9292, 8:0.9306, 9:0.9319},'3dp':{1:1, 2:3, 3:4, 4:6, 5:7, 6:8, 7:10, 8:11, 9:13}},
          1.5 : {'2dp':{0:0.9332, 1:0.9345, 2:0.9357, 3:0.9370, 4:0.9382, 5:0.9394, 6:0.9406, 7:0.9418, 8:0.9429, 9:0.9441},'3dp':{1:1, 2:2, 3:4, 4:5, 5:6, 6:7, 7:8, 8:10, 9:11}},
          1.6 : {'2dp':{0:0.9452, 1:0.9463, 2:0.9474, 3:0.9484, 4:0.9495, 5:0.9505, 6:0.9515, 7:0.9525, 8:0.9535, 9:0.9545},'3dp':{1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}},
          1.7 : {'2dp':{0:0.9554, 1:0.9564, 2:0.9573, 3:0.9582, 4:0.9591, 5:0.9599, 6:0.9608, 7:0.9616, 8:0.9625, 9:0.9633 },'3dp':{1:1, 2:2, 3:3, 4:4, 5:4, 6:5, 7:6, 8:7, 9:8}},
          1.8 : {'2dp':{0:0.9641, 1:0.9649, 2:0.9656, 3:0.9664, 4:0.9671, 5:0.9678, 6:0.9686, 7:0.9693, 8:0.9699, 8:0.9706},'3dp':{1:1, 2:1, 3:2, 4:3, 5:5, 6:4, 7:5, 8:6, 9:6}},
          1.9 : {'2dp':{0:0.9713, 1:0.9719, 2:0.9726, 3:0.9732, 4:0.9738, 5:0.9744, 6:0.9750, 7:0.9756, 8:0.9761, 9:0.9767},'3dp':{1:1, 2:1, 3:2, 4:2, 5:3, 6:4, 7:4, 8:5, 9:5}},
          2.0 : {'2dp':{0:0.9772, 1:0.9778, 2:0.9783, 3:0.9788, 4:0.9793, 5:0.9798, 6:0.9803, 7:0.9808, 8:0.9812, 9:0.9817},'3dp':{1:0, 2:1, 3:1, 4:2, 5:2, 6:3, 7:3, 8:4, 9:4}},
          2.1 : {'2dp':{0:0.9821, 1:0.9826, 2:0.9830, 3:0.9834, 4:0.9838, 5:0.9842, 6:0.9846, 7:0.9850, 8:0.9854, 9:0.9857},'3dp':{1:0, 2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:4}},
          2.2 : {'2dp':{0:0.9861, 1:0.9864, 2:0.9868, 3:0.9871, 4:0.9875, 5:0.9878, 6:0.9881, 7:0.9884, 8:0.9887, 9:0.9890},'3dp':{1:0, 2:1, 3:1, 4:1, 5:2, 6:2, 7:2, 8:3, 9:3}},
          2.3 : {'2dp':{0:0.9893, 1:0.9896, 2:0.9898, 3:0.9901, 4:0.9904, 5:0.9906, 6:0.9909, 7:0.9911, 8:0.9913, 9:0.9916},'3dp':{1:0, 2:1, 3:1, 4:1, 5:1, 6:2, 7:2, 8:2, 9:2}},
          2.4 : {'2dp':{0:0.9918, 1:0.9920, 2:0.9922, 3:0.9925, 4:0.9927, 5:0.9929, 6:0.9931, 7:0.9932, 8:0.9934, 9:0.9936},'3dp':{1:0, 2:0, 3:1, 4:1, 5:1, 6:1, 7:1, 8:2, 9:2}},
          2.5 : {'2dp':{0:0.9938, 1:0.9940, 2:0.9941, 3:0.9943, 4:0.9945, 5:0.9946, 6:0.9948, 7:0.9949, 8:0.9951, 9:0.9952},'3dp':{1:0,2:0, 3:0, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}},
          2.6 : {'2dp':{0:0.9953, 1:0.9955, 2:0.9956, 3:0.9957, 4:0.9959, 5:0.9960, 6:0.9961, 7:0.9962, 8:0.9963, 9:0.9964},'3dp':{1:0, 2:0, 3:0, 4:0, 5:1, 6:1, 7:1, 8:1, 9:1}},
          2.7 : {'2dp':{0:0.9965, 1:0.9966, 2:0.9967, 3:0.9968, 4:0.9969, 5:0.9970, 6:0.9971, 7:0.9972, 8:0.9973, 9:0.9974},'3dp':{1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:1, 8:1, 9:1}},
          2.8 : {'2dp':{0:0.9974, 1:0.9975, 2:0.9976, 3:0.9977, 4:0.9977, 5:0.9978, 6:0.9979, 7:0.9979, 8:0.9980, 9:0.9981},'3dp':{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:1, 9:1}},
          2.9 : {'2dp':{0:0.9981, 1:0.9982, 2:0.9982, 3:0.9983, 4:0.9984, 5:0.9984, 6:0.9985, 7:0.9985, 8:0.9986, 9:0.9986},'3dp':{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}}
          }
        
        z_val = str(zval)#converts integer into string for easy manipulation
        if len(z_val)==5:
            key1 = eval(z_val[0:3])
            r1 = z_score[key1] n    
            prob_inc1 = r1['2dp'][eval(z_val[3])] #incomplete probability
            prob_inc2= r1['3dp'][eval(z_val[4])]
            prob= prob_inc2*0.001 + prob_inc1
            #return(probability)
        elif len(z_val)==4:
            key1 = eval(z_val[0:3])#slices the string to 1dp
            r1 = z_score[key1]#gives the dictionary of dictionary with key key1
            prob = r1['2dp'][eval(z_val[3])]
            #return(probability)
        elif len(z_val)==3:
            key1 = eval(z_val[0:3])#slices the string to 1dp
            r1 = z_score[key1]
            prob = r1['2dp'][0]
        
        return prob



''' this function reads the corresponding probability of a z_value from the normal distribution table
parameters: mean, standard deviation and X, the instance
returns the value of the probability as read from the table'''
        
def normal1(mean, s_d, x):
        z = round(((x-mean)/s_d),3) # round to 3dp
        if z < 0:
                p_up = phi(abs(z))#phi is called within normal, which means abs(z) = zval
                p_down = 1-p_up
                probability = {'p(Z<-z)':p_up,'p(Z>-z)':p_down}
         else:
                 p_down = phi(z)
                 p_up = 1-phi(z)
                 probability = {'p(Z>z)':p_up,'p(Z<z)':p_down}
        return probability


''' this function works like the previous function but now the probability is calculated between two limits.
it returns the probability associated with the z_scores.
parameters: mean, standard deviation, with X and Y being the limits.'''
def normal2(mean,s_d,x,y):
    z_score1 = round((x-mean/s_d),3)
    z_score2 = round((y-mean/s_d),3)
    if z_score1 or z_score2 < 0:
        p_down = phi(abs(z_score1)) + phi(abs(z_score2)) - 1 # this means that since phi has been invoked, abs(z_score1) and abs(z_score2) are now the parameters for phi
        probability = {'p(-z1<Z<z2)':p_down}
    elif z_score1 == z_score2 and z_score1 == -1*z_score2:
        p_down = 2*phi(abs(z_score1)) - 1
        probability = {'p(-z<Z<z)': p_down}
    elif z_score1 and z_score2 < 0:
        p_down = phi(abs(z_score1)) - phi(abs(z_score2))
        probability = {'p(-z1<Z<z2)': p_down}
    return probability
        

''' this function returns the probability using poisson distribution
parameters: mean(L) and X, the instance
returns probability

E_x = L
var_x = L'''
def poisson(L,x):
    exactly_x= math.exp(-L)*(L**x/math.factorial(x))
    return{"Expectation E(x)":L,"variance var(x)":L,"p(exactly x)":exactly_x}
# At least x
def At_least_x(n):
        probability = 0
        for i in range(0,n):
                exactly_x= math.exp(-L)*(L**x/math.factorial(x))
                probability = probaility + exactly_x
        At_least_x = {'At_least_x':1-probability}
        return At_least_x

def At_most_x(n):
        

# Exponential distribution
# X follows an exponential distribution with mean lambda

def exponential(L,x):
    exactly_x= 1 - math.exp(-L*x)  # this is supposed to be for p(X<x)
    #p(X>x) = math.exp(-L*x)
    #p(x1 <X< x2) = math.exp(-L*x1) - math.exp(-L*x2)
    E_x = 1/L
    var_x = 1/L**2
    return{"Mean E(x)":E_x,"Variance Var(x)":var_x,"p(exactly x)":exactly_x}
    
  


# Geometric distribution
#X follows a geometric distribution with probability of success of p

def geo(p,x):
    p_down1 = 1-(1-p)**x
    p_up1 = (1-p)**(x-1)
    p_down = 1-(1-p)**(x-1)
    p_up = (1-p)**x
    E_x = 1/p
    Var_x = 1-p/p**2
    return{"Mean E(x)": E_x,"Variance var_x":Var_x,"p(X<=x)":p_down1,"p(X>=x)":p_up1,"p(X<x)":p_down,"p(X>x)":p_up } 
    
    
