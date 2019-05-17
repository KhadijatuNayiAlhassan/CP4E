from CPA6_functions import find_sum
def main():
    n = input("please enter a number: ")
    if len(n) > 0: # the function is only invoked if input is not void
        print(find_sum(n))
        
    else: # empty string denotes void input
        print('please enter a number, your input is void')
main()