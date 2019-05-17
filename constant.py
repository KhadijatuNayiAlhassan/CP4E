
def reverse_name(name):
    rev_name = ""
    for i in range(1,len(name)+1):
        rev_name = rev_name+name[-i]
    return rev_name
print(reverse_name("Khadijatu"))
