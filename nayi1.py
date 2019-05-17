#   question 1
def find_len(sentence):
    list1 = sentence.split()
    word =list1[-1]
    return len(word)

#question2
def find_num(p):
    i = p
    
    while i and i > 1:
        if i%2 == 0 :
            a = i/2
            print(a,end = ",")
            # print(a)
    
        elif i%2 != 0:
            a = 3*i+1
            print(a,end = ",")
            # print(a)
        i = a

#Question3
#def sum_reverse(num1,num2):
    #num
        
        
            
