from string import punctuation

def divBy7():
    myList = []
    x = list(range(2000,3200+1))
    for number in x:
        if number % 7 == 0 and number % 5 != 0:
           
            myList.append(number) #print(number, end = ',')
    print(myList)

    

divBy7()
   
def numN ():
    n = int(input("enter a number"))
    myDict = {}

    for i in range(1, n+1): #1, 2, 3, ....n 
       myDict[i]= i*i
    print(myDict)   
numN ()

def Let () :
    n = int(input("enter a number"))
    newDict = {}
    for i in range(1, n+1):
        if i % 2 ==1:
            newDict[i]=i*i
    print(newDict)
            
Let ()

y=list(punctuation)

def sent () :
    s = input("enter a sentence: ")
    count = 0
    letter=0
    num_digits=0
    digits = '0123456789'
    for character in s:
        if character != ' ' and character not in y:
            if character not in digits :
                letter=letter+1
            else:
                num_digits=num_digits+1
          
    print("letter = ",letter)
    print( "number = ",num_digits)
sent ()

