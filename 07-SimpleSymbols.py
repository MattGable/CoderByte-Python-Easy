'''
From CoderByte: "Using the Python language, have the function SimpleSymbols(str)
take the str parameter being passed and determine if it is an acceptable
sequence by either returning the string true or false. The str parameter
will be composed of + and = symbols with several letters between them
(ie. ++d+===+c++==a) and for the string to be true each letter must be
surrounded by a + symbol. So the string to the left would be false.
The string will not be empty and will have at least one letter."

'''

#1-Iterate over the string and make sure all alpha chars have + on each side.
#2- Also scan the string to make sure it only contains letters, +, and =.
#3- Empty strings and strings with 0 letters are also false.
#Return either the valid string or an error message. If there is an error,
#simple_symbol simply returns the first one it encounters.
#This script returns errors as strings rather that raise Exception("Error!").


def simple_symbol(string):

    #Check for zero string length
    if len(string) == 0:
        return "Error: String length is 0"

    #Check for both + and = in string
    if not "+" in string or not "=" in string:
        return "Error: No + or ="

    #Now check to make sure there's at least one letter
    for i in range(len(string)):

        if string[i].isalpha():
            print string[i].isalpha()
            print i
            break
        elif i == len(string)-1:
            return "Error: There are no alpha characters"

    #Now checking to make sure each letter is surrounded by "+"
    for i in range(len(string)):

        if string[i].isalpha() == False and string[i] != "+" and string[i] != "=":
            return "Error: Illegal characters"
        elif string[i].isalpha() and i == 0:
            return "Error: Your first character is a letter"
        elif string[len(string)-1].isalpha():
            return "Error: Your last character is a letter"
        elif string[i].isalpha() and string[i-1] != "+" and i >= 0:
            return "Error: Letter is missing a + to its left"
        elif string[i].isalpha() and string[i+1] != "+":
            return "Error: Letter is missing a + to its right"

    return string

    


print simple_symbol("++b+==+b+++===+b+")

