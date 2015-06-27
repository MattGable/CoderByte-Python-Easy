'''
From CoderByte: "Using the Python language, have the function
AlphabetSoup(str) take the str string parameter being passed
and return the string with the letters in alphabetical order
(ie. hello becomes ehllo). Assume numbers and punctuation symbols
will not be included in the string."
'''
#1-Take in string str
#2-Alphabetize str (taking advantage of built-in sort)
#R-Return the alphabetized string
def alphabet_soup(string):

    #sort/alphabetize string
    sorted_list = sorted(string)
    #Convert the list from sorted() back into string
    return_string = ''.join(sorted_list)
    return return_string
        

print alphabet_soup("hello")

