from Khadijatu_Alhassan_Python_final import Probability
prob = Probability()
mean = 30
sd = 4
x1 = 40
x2 = 30
x3 = 35
#test for normal distribution
n1= prob.normal_dist1(mean,sd,x1)
print(n1)
n2 = prob.normal_dist2(mean,sd,x2,x3)
print(n2)

#test for geometric distribution
geo = prob.geometric(0.8,3)
print(geo)

# test for exponential distribution
expo = prob.exponential(0.125,5)
print(expo)

#test for poisson distribution
poi = prob.poisson(1.95,3)
print(poi)

