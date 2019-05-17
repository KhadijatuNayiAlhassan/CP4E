# test for normal distribution
from my_python_project import phi,normal,poisson,geo,exponential
#phi(zval)
print(normal(10,5,2))# gives z_value = -1.6
print(normal(30,4,40))# gives z_value = 2.5
print(normal(30,4,21))#gives z_value = -2.25
print(normal(30,4,27.5))#gives z_value = -0.625


#test for poisson distribution
print(poisson(0.1,7))


#test for exponential distribution
print(exponential(0.2,5))


#test for geometric distribution
print(geo(1/6,5))
