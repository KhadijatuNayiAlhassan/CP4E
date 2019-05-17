'''Author: Khadijatu Nayi Alhassan
 CPA6'''


def find_sum(n):
    '''This function takes find the sum of the digits that make up a number.
    paramters: 
        n: a whole number
    returns a sum of the digits in n'''
    
    try:
        ''' This part of the code deals with handling errors. It prints a statement
        to guide the user to enter the right input if he enters a decimal number,
        a negative number or a void input'''
        sum_num = 0
        let = str(n)

        for i in let:
            num = int(i)
            sum_num +=num
        return sum_num

    except SyntaxError:
        print('please enter a whole number')
    except ValueError:
        print("your input contains a character other than an integer")
    except TypeError:
        print('please enter a number, your input is void')


    



