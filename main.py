
'''
UNDERSTAND:
- input: string 
- return a new string with letters replaced by next letters in alphabet

PLAN:
- for loop to loop through every character in the string
- use the strip() function to return a copy of inputString in which all characters have been stripped from the beginning and the end of the string (default whitespace characters)
- create new string to store the letters stripped from inputString. 
- join the string together




'''


def alphabeticShift(inputString):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabc'
    l = list(alphabet)
    new_string = []
    
    for letter in list(inputString.lower().strip()):
        new_string.append(l[alphabet.index(letter) + 1])
    new_string = "".join(new_string)
    return new_string
    print(l)
    print(inputString)
    new_string = [char for char in inputString]
    print(new_string)
    
    
   

