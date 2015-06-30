'''
From CoderByte: "Using the Python language, have the function ArithGeo(arr)
take the array of numbers stored in arr and return the string "Arithmetic"
if the sequence follows an arithmetic pattern or return "Geometric" if it
follows a geometric pattern. If the sequence doesn't follow either pattern
return -1. An arithmetic sequence is one where the difference between each
of the numbers is consistent, where as in a geometric sequence, each term
after the first is multiplied by some constant or common ratio. Arithmetic
example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. Negative numbers
may be entered as parameters, 0 will not be entered, and no array will contain
all the same elements. 
'''
#1-Take a list as an input
#2-Using the first two values, establish a potential constant
#3-Count each value in the list that holds to either an 
#additive constant or a multiplicative constant and
#retun true if all values do (excluding the first value)
#Return -1 if both tests are untrue

#NOTE: This code assumes a list is entered. It also returns
#an error message for a list of length 0 or 1. 


def arith_geo(list1):

    #Catch lists with fewer than two items
    if len(list1) <= 1:
        return "The list is too short"

    #Find a potential additive constant in the list for comparison
    pot_add_const = list1[1] - list1[0]
    #A counter for the terms following the constant
    add_count = 0

    for i in range(len(list1)):
        if i > 0 and list1[i] - list1[i-1] == pot_add_const:
            add_count += 1
        if add_count == len(list1) - 1:
            return "Arithmetic"
    
    #Find a potential multiplicative constant in the list for comparison
    pot_mult_const = float(list1[i]) / float(list1[i-1])
    #A counter for the terms following the constant
    mult_count = 0
    
    for i in range(len(list1)):
        if i > 0 and float(list1[i]) / float(list1[i-1]) == pot_mult_const:
            mult_count += 1
        if mult_count == len(list1) - 1:
            return "Geometric"
        
    #Return -1 if both iterative searches are false
    return -1
        


print arith_geo([2, 4, 6, 8])

