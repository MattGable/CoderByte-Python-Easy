'''
From CoderByte: "Using the Python language, have the function WordCount(str)
take the str string parameter being passed and return the number of words
the string contains (ie. "Never eat shredded wheat" would return 4).
Words will be separated by single spaces."
'''
#1-Get the string input
#2-Count the first letter as a word if there is no space in front
#3-Count subsequent words by counting letters with a space in front
#Return the number of words
#NOTE: According to the problem definition, only 1 space between words
#is assumed for the input, so no checks are here for multiple spaces, etc.! 

def word_count(string):

    num_of_words = 0
    for i in range(len(string)):
        #Check to see if first letter is an alpha
        if i == 0 and string[0].isalpha():
            num_of_words += 1
        #Check for letters with a space in front of them
        if i > 0 and string[i].isalpha and string[i-1] == ' ':
            num_of_words +=1
            

    return num_of_words

print word_count("Never eat shredded wheat")



