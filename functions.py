'''Author: Khadijatu Nayi Alhassan
CPA4'''
# Question 1
def letter_to_index():
    x = input('enter a letter: ')# takes a letter as input
    print(ord(x))#prints the corresponding index of the letter according to
                #ASCII

    
#Question 2
def index_to_letter():
    x = int(input('enter a number: '))# takes a number as input and prints the
                                      #corresponding character
    print(chr(x))

    
#Qustion 3
def grade(test_score):     # this function takes a test_score and prints the
                           #grade it matches with.

    if 80 <= test_score <= 100:
        print("A")
    elif 75 <= test_score <= 79:
        print("B+")
    elif 70 <= test_score <= 74:
        print("B")
    elif 65 <= test_score <= 69:
        print("C+")
    elif 60 <= test_score <= 64:
        print("C")
    elif 55 <= test_score <= 59:
        print("D+")
    elif 50 <= test_score <= 54:
        print("D")
    else:
        print("E")

#test
def main():
    letter_to_index()
    index_to_letter()
    grade(76)
main()
