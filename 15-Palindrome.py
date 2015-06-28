'''
FromCoderByte: "Using the Python language, have the function Palindrome(str)
take the str parameter being passed and return the string true if the
parameter is a palindrome, (the string is the same forward as it is
backward) otherwise return the string false. For example: "racecar"
is also "racecar" backwards. Punctuation and numbers will not be part
of the string. 
'''

#NOTE: Again, data entry errors are assumed away in the problem, so this code
#does not catch numbers, etc. However, the problem did not assume away capital
#letters, so a catch for those is in the code.

def Palindrome(string):

    if string.lower() == string[::-1].lower():
        return "true"
    else:
        return "false"

print Palindrome("rAceCar")


