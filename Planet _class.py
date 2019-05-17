import math
class Planet:
    def __init__(self,radius,mass,name):
        self.radius = radius
        self.mass = mass
        self.name = name
        
    def getRadius(self):
        return self.radius
    
    def setRadius(self, radius):
        self.radius = radius
        
    def getMass(self):
        return self.mass
    
    def setMass(self,mass):
        self.mass = mass
        
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getDensity(self):
        volume = (4/3) * self.radius**3
        density = self.mass/volume
        return density
    
    def getSurfaceArea(self):
        surfaceArea = 2*math.pi*self.radius**2
        return surfaceArea
        
a= Planet(100,200,'Venus')
print(a.getRadius())

#creating a student class

class Student:
    def __init__(self,name,ID,major,age):
        self.name = name
        self.ID = ID
        self.major = major
        self.age = age
        #print('Student details:' +  self.name + ' '+  str(self.age) + ' ' + self.major)
        
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name

    def getID(self):
        return self.ID  

    def setID(self,ID):
        self.ID = ID

    def getMajor(self):
        return self.major 

    def setMajor(self,major):
        self.major = major

    def getAge(self):
        return self.age

    def setAge(self,age):
        self.age = age
vera = print(Student('Vera','12342022','ME',18))#creates an instance of the class

