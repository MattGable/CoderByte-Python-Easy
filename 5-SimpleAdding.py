'''
From CoderByte: "Using the Python language, have the function SimpleAdding(num)
add up all the numbers from 1 to num. For the test cases,
the parameter num will be any number from 1 to 1000."
'''
#1-Add up all the numbers from 1 through num (no more than 1000).
#Return - The result of the addition

def simple_adding(num):
    num_holder = 0
    for i in range(num):
        i = i + 1
        num_holder += i
    return num_holder


print simple_adding(12)
