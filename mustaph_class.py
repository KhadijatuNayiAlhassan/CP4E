class WashMachine:
    def __init__(self,water_temp,cloth_weight):
        self.water_temp = water_temp
        self.cloth_weight = cloth_weight

    def getWaterTemp(self):
        return self.water_temp

    def setWaterTemp(self,water_temp):
        self.water_temp = water_temp

    def getClothWeight(self):
        return self.cloth_weight 

    def setClothWeight(self,cloth_weight):
        self.cloth_weight = cloth_weight

        if water_temp == 1:
            a = 1
            b = 2
            c= 4

            if self.cloth_weight<10:
                print(str(a) + " cup of detergent should be used")
                num_cups = a
                return num_cups 

            elif self.cloth_weight>=10 and self.cloth_weight<25:
                print(str(b) +" cups of detergent should be used")
                num_cups = b
                return num_cups

            elif self.cloth_weight>25:
                print(str(f)+" cups of detergent should be used")
                num_cups = f
                return num_cups