''' Author: Khadijatu Nayi Alhassan
'''
''' this function takes two lists, takes the
entries in one as the keys and assign the entries of
the other as values.
parameters: two lists
returns a dictionary'''

##name_list = ['joe','tom','barb','sue','sally']
##score_list = [10,23,13,18,12]
##def makeDictionary(name_list, score_list):
##     dict = {}
##     for i in range(len(name_list)):
##         dict[name_list[i]] =(score_list[i])
##     print(dict)
##makeDictionary(name_list,score_list)
##        
#evaluating the mode of a given set of data
'''This function takes a list of numbers and computes the mode
parameter : list of numbers
returns a dictionary
'''
##def mode_of_list(alist):
##    count_dict = {}
##    for i in alist: # looks at each value in new_list
##        if i in count_dict:
##            count_dict[i] =+1 #if i is in count-list, it means that i has
##                              #been counted, so the frequency increases by 1
##        else:
##            count_dict[i] = 1
##    return count_dict
##mode_of_list([5,2,3,1,5,6,9,3,2,2,1])


def aziz(alist):
    alist = list(alist)
    counter = {}
    for i in alist:
        if i in counter:
            counter[i] =+ 1
        else:
            counter[i] = 1
    return counter
    
