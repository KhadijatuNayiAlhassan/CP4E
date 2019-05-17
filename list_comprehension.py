
''' Author: Khadijatu Nayi Alhassan
'''
# to break a code, use ctrl + c

## w = []
## for i in range(20):
##     if i%2 == 0:
##         w.append(i)
##     return w
##
## using list comprehension
##print([i for i in range(20)
##    #if i%2==0])
##
## trial for midsem exam
##Question 1
##''' this function returns a set minus duplicates
##parameter: list
##returns a list '''
##def list_minus_duplicates(alist):
##     alist = set(alist)
##     return alist
##list_minus_duplicates(["Ama","Cynthia","Kofi","Esi","Ama","Frank","Grace","Frank","Aseda","Ama","Patience"])
##
##
###question 2
##''' this function takes several dictionaries and concatenates them to form
##one.
##parameters: Dictionaries
##returns a dictionary'''
##dictA={1:5, 2:10}
##dictB={3:15, 5:25}
##dictC={8:40, 9:45,11:55}
##dictD={15:75,16:80}
##dictE={19:95,20:100}
##dictF={19:20,20:100}
##listA = [dictA,dictB,dictC,dictD,dictE,dictF]
##
##def concat_dict(list_dict):
##    
##    dictA = list_dict[0]
##    for item in list_dict:
##        dictA.update(item)
##    return dictA
##
##
##print(concat_dict(listA))
##
###question 3
##''' this function loops through a range of numbers and return
##all numbers that are divisible by 7 but not divisible by 5
##parameter: none
##returns a list of numbers'''
##def num_finder():
##    list1 = []
##    for i in range(2000,3201):
##        if i%7 ==0 and i%5!=0:
##            list1.append(i)
##    return list1
##print(num_finder())

###question 4
##'''this function creates a dictionary of number: number squared
##parameter: number
##returns a dictionary'''
##def dict_num_squared(n):
##     dict1 = {}
##     i = 1
##     while i<=n:
##         dict1[i]=i**2
##         i = i+1
##     return dict1
##print(dict_num_squared(8))
import string
# question 5
''' this function takes a sentence and counts the number of letters and numbers in it
parameters: string
returns letter count and number count
'''
'''def num_let_count(sentence):
    alphabets = string.ascii_letters
    digits = string.digits
    Letter_count = 0
    Num_count = 0
    for i in sentence:
        if i in alphabets:
            Letter_count =+1
    return Letter_count
        elif i in digits:
            Num_count =+1
    return Num_count
    return({"Letters":Letter_count,"Numbers":Num_count})
print(num_let_count("Hello sis123@!"))'''

'''this function takes a word and returns the word without vowels
parameters: word in string form
returns a word as a string'''
'''def getVwls(word):
    word_wo_vowels = ''
    vowels = 'aeiouAEIOU'
    for i in word:
        if i  not in vowels:
            word_wo_vowels = word_wo_vowels + word[word.index(i)]
    return word_wo_vowels
print(getVwls('University'))'''

''' this function returns the sum of the indices of a name
parameters: name
reurns a number '''

##def name_value(name):
##    numeric_value = 0
##    alphabets = ' abcdefghijklmnopqrstuvwxyz'
##    for i in name:
##        numeric_value = numeric_value + alphabets.index(i)
##    return numeric_value
##print(name_value('zelle'))
        
#print(__builtins__)
'''import string
def charCount(sentence):
    chrcount = 0
    char = (string.printable)
    for i in sentence:
        if i in char:
            chrcount = +1
    return chrcount
print(charCount('hello sis 12!'))'''

'''this code takes a csv file and returns a list of the marks of students'''

##marks = []
##with open('quiz.csv','r') as file:# can also be written as file = open('quiz.csv,'r'')
##    for line in file:
##        list1 = line.split(',')
##        marks = marks.append(list1[1])
##    close
        
'''the whole point of classes is to model a real world object. for eg. students have attributes name, age,sex,major,class,Id etc. these attributes are called instance variables.
a student can do ceratin things(actions). these are called methods. mutators are methods that can change attributes.'''
             
''' this function takes a sentence and returns the number of characters without spaces
parameter: sentence
returns a number'''
# def charcount(sentence):
#     chars = sentence.replace(' ','')
#     return len(chars)
# charcount('hello sis 123')


# ''' writing a function without using print and input in the function itself'''
# from random import randint
# def getNumber(guess, ranNum):
#     if guess > ranNum:
#         return 1
#     if guess < ranNum:
#         return -1
#     else:
#         return 0

# def main():
#     a = randint(1,20)'''this code returns one value every time, if we want
#                      it to generate a different number each time, we need to use
#                      a loop'''
   
#     guessed = False   #initialises while loop, assuming person has not guessed
#     while not guessed: # while true, evaluate the code
#          userguess = int(input('please guess a number'))
#          result = getNumber(userguess,a)
#          if result == 0:
#              print('Yaaay! ypu guessed it right')
#              guessed = True #we need to terminate the code if the person got it right
#         elif result == -1:
#             print('You guessed too low')
#         elif result == 1:
#             print('You guessed too high')
            
# main()
#     def pattern(n):
#     m = n//2
#     for i in range(1,m+2):
#         print('*'*i)

#     for j in range(-m,0):
#         print('*'*abs(j))

# p = "justice"

# even = ''
# odd = ''
# for i in (len(p)):
#     if i%2 == 0:
#         even = even + p[i]
#     else:
#         odd = odd +p[i]
# print(even)
# print(odd)

def mode(dataList):
    m = {}
    for num in dataList:
        if num in m:
            m[num] +=1
        else:
            m[num]=1
    print(m)
mode([2,2,0,4,5,7,9,8,7,6,6,3,1,9])




    
