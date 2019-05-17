def fxn():
    file = open("CPA5_functions.txt","r")
    list1 = []
    for line in file:
        values = line.split(",")
        list1.append(values[1])
    return list1
#print(fxn())

def word_count(sentence):
    words = sentence.split()
    return len(words)
#print(word_count("I am a boy"))

def char_count(sentence):
    chars = sentence.replace(" ","")
    return len(chars)
#print(char_count("i am a boy!!!"))

def num_print(num):
    num_list = []
    for i in range(num+1):
        if i ==3 or i ==6:
            continue
        else:
            num_list.append(i)
    return num_list
#print(num_print(6))

def fibonacci(n):
    #list1 = [0,1]
    dict1 = {0:0, 1: 1} 
    
    for i in range(2,n+1):
        # fib_i = list1[i-1]+list1[i-2]
        # list1.append(fib_i)
        dict1[i] = dict1[i-2]+dict1[i-1]
    # print(dict1[19])
    # print(dict1[30])
    # print(dict1[9])
    print(sorted(dict1.items(), reverse = True, key=lambda t: t[1]))
    

    return dict1
    #return list1[n-1]

fibonacci(30)

