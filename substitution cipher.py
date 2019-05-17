import random
def key_gen():
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    key = ''
    for i in range(len(alphabets)):
        char_in_key = random.randint(0,25-i)#0 - 25 gives 26
        
        key = key + alphabets[char_in_key]
        alphabets.pop(char_in_key)
    print(key)

key_gen()
        
