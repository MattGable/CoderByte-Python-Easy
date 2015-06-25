'''
From CoderByte: Using the Python language, have the function
CheckNums(num1,num2) take both parameters being passed and return the
string true if num2 is greater than num1, otherwise return the string false.
If the parameter values are equal to each other then return the string -1. 
'''

#1-Compare num1 and num2. Return true as a string if num2 > num1.
#2-Otherwise, return false--also as a string.
#Return - "true" or "false" per the rules above.

def check_nums(num1, num2):
    if num2 > num1:
        return "true"
    elif num2 <= num1:
        return "false"
    else:
        return "Something else went wrong..."


print check_nums(3, 3)

