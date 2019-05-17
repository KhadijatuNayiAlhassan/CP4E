from final import Probability

prob = Probability()
mean = 30
sd = 4
x1 = 40
x2 = 30
x3 = 35
test for normal distribution
print("Normal distribution",end = "***************")
print("")
n1= prob.normal_dist1(mean,sd,x1)
print(n1)
n2 = prob.normal_dist2(mean,sd,x2,x3)
print(n2)
print(" ")

#test for geometric distribution
print("geometric distribution",end ="*******************")
print("")
geo = prob.geometric(0.8,3)
print(geo)
print(" ")

# test for exponential distribution
print("Exponential distribution",end = "*******************")
print("")
expo = prob.exponential(0.125,5)
print(expo)
print(" ")

#test for poisson distribution
print("Poisson distribution",end = "******************")
print("")
poi = prob.poisson(1.95,3)
print(poi)
print(" ")


prob.normal_dist1(mean,sd,30)
prob.plot_norm_dist(mean, sd, shade_bw= "20,40")
