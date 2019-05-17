def scramble2encrypt(plaintext):
     evenChars = ""
     oddChars = ""
     charCount = 0
     for ch in plaintext:
         charCount = charCount + 1
         if charCount % 2 == 0:
             evenChars = evenChars + ch
         else:
             oddChars = oddChars + ch
     ciphertext = oddChars + evenChars
     print(ciphertext)
     print(charCount)
 #scramble2encrypt( "Khadijatu Nayi")

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
    print("LETTERS: " + str(alpha_count))
    print("Digits: " + str(num_count))
##len_alpha_num("hello world 123")

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

##def next_date():
##    try:
##        year = input("Please enter the year: ")
##        month = input("Please enter the month,1-12: ")
##        day = input("Please enter the day: ")
##        date = year + "-"+ month +"-" + str((int(day)+1))
##        #print(date)
##        
##    except:
##        if year not in range(1,13):
##            print("month must be between 1 and 12")
##    except:
##        if day not in range(1,32):
##            print("day must be between 1 and 31")
##        
##    return date

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

# def season(month,day):
#     month = {"JAN":1,31"FEB":2,29"MAR":3,31"APR":4,30"MAY":5,31"JUN":6,30"JUL":7,31
#     "AUG":8,31"SEPT":9,30"OCT":10,31"NOV":11,30"DEC":12,31}
#     spring = MAR 1 - APR 31
#     summer = JUN 1- AUG 31
#     autumn = SEPT 1 - NOV 30
#     winter = DEC 1 - FEB 29

def num_checker():
    word = input("please enter a word: ")
    numbers = ["one","two","three","four","five","six","seven","eight","nine"]
    num_notation = ["hundred","thousand","million","billion","trillion","zillion"]
    word_list = word.split()
    #if len(word_list) == 1:

    for i in word_list:
        if i not in numbers or num_notation:
    print(word + " is not an integer")
           
    
num_checker()
        








        
