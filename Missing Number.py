##def MissingNumber(x):
##    for i in range [x]:
##        n = x[0]
##        if x[i] == n + 1:
##            n = n + 1
##            print(n)
##        else:
##            print (n + 1)
##
##MissingNumber(list('12346789'))

'''this function returns the missing number in a list.
parameter:
list of consecutive numbers
Return:
missing number or "list correct"
'''
def missing_num_finder(L1):
    num_1 = L1[0]
    num_last = L1[-1]
    for i in range(num_1,num_last):
        if i not in L1:
            return i

    return "list correct"


print(missing_num_finder([0,1,3]))
print(missing_num_finder([100,101,102,103]))


###central tendency
##
##def get_median(alist):
##    alist.sort()
##    if len(alist)%2 != 0:
##        #print(len((alist)+1)/2)
##        median = alist[((len(alist)+1)/2
##    else:
##        #median = alist[len(alist)/2] + alist[(len(alist)+1)/2]
##    print(median)
##get_median([1,2,5,4,8])
