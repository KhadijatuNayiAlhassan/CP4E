# def scramble2encrypt(plaintext):
#     evenChars = ""
#     oddChars = ""
#     charCount = 0
#     for ch in plaintext:
#         charCount = charCount + 1
#         if charCount % 2 == 0:
#             evenChars = evenChars + ch
#         else:
#             oddChars = oddChars + ch
#     ciphertext = oddChars + evenChars
#     print(ciphertext)
#     print(charCount)
# scramble2encrypt( "Khadijatu Nayi")

def sum_of_multiples(limit):
    sum = 0
    for i in range(limit+1):
        if i%3 == 0 or i%5 == 0:
            sum= sum+i
    return sum
#print(sum_of_multiples(20))

def len_alpha_num(sentence):
    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    alpha_count = 0
    num_count = 0
    for i in sentence:
        if i in alphabets:
            alpha_count+=1
        elif i in digits:
            num_count+=1
    #print("LETTERS: " + str(alpha_count))
    #print("Digits: " + str(num_count))
#len_alpha_num("hello world 123")

#python trial questions
def pattern(n):
    for i in range(1,n+1):
        print(str(i)*i)
#pattern(7)

def mult_table(n):
    for i in range(1,11):
        line = str(n)+" x "+ str(i)+" = "
        print(line,n*i)
    return(line,n*i)

#(mult_table(6))

def next_date():
    year = input("Please enter the year: ")
    month = eval(input("Please enter the month,1-12: "))
    day = eval(input("Please enter the day: "))

    if month not in list(range(1,13)):
        print("month must be between 1 and 12")
    elif day not in list(range(1,32)):
        print("day must be between 1 and 31")
    else:
        date = year + "-"+ str(month) +"-" + str((int(day)+1))
        print(date)
    

#next_date()

def find_median(list1):
    list1.sort()
    num = round(len(list1)/2)
    if len(list1)%2 != 0:
        median = list1[num]
        return median
        
    elif len(list1)%2 == 0:
        num1 = int(len(list1)/2)+1
        med = (list1[-num]+list1[-num1])/2
        return med
        
        
    
#rint(find_median([1,5,2,1,9,6]))

def season():
    # month = {"JAN":(1,31), "FEB":(2,29), "MAR":3,31"APR":4,30"MAY":5,31"JUN":6,30"JUL":7,31
    # "AUG":8,31 "SEPT":9,30 "OCT":10,31 "NOV":11,30 "DEC":12,31}
    # spring = MAR 1 - APR 31
    # summer = JUN 1- AUG 31
    # autumn = SEPT 1 - NOV 30
    # winter = DEC 1 - FEB 29
    seasons = {"winter":["JANUARY","FEBRUARY","DECEMBER"],"summer":["JUNE","JULY","AUGUST"],
    "autumn":["SEPTEMBER","OCTOBER","NOVEMBER"],"spring":["MARCH","APRIL"]}
    month = input("please enter a month: ")
    month = month.upper()

    if month in  seasons["winter"]:
        print("season is winter")
    elif month in seasons["summer"]:
        print("season is summer")
    elif month in seasons["autumn"]:
        print("season is autumn")
    elif month in seasons["spring"]:
        print("month is spring")
#season()
def num_checker():
    word = input("please enter a word: ")
    numbers = ["one","two","three","four","five","six","seven","eight","nine"]
    num_notation = ["hundred","thousand","million","billion","trillion","zillion"]
    word_list = word.split()

    is_int = False
    for i in word_list:
        if i in numbers or i in num_notation:
            is_int = True
        else:
            is_int = False
            break

    if is_int == True:
        print(word + " is an integer")
    else:
        print(word + " is not an integer")
    
num_checker()

def sum_num(num1, num2):
    add = num1 + num2
    if add in range(15,21):
        return 20
    else:
        return add
#print(sum_num(18,25))
#print(sum_num(10,5))
#print(sum_num(5,7))

    seasons = {"winter":[1,2,3],"summer":[6,7,8],
    "autumn":[9,10,11],"spring":[3,4]}

    month = int(input("please enter a month: "))
    day = int(input("please enter a day"))

    
    
    if month in  seasons["winter"]:
        if day in range(1,32):
            print("season is winter")
    elif month in seasons["summer"]:
        print("season is summer")
    elif month in seasons["autumn"]:
        print("season is autumn")
    elif month in seasons["spring"]:
        print("month is spring")
#season()






        
