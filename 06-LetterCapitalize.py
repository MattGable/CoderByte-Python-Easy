'''
From CoderByte: "Using the Python language, have the function LetterCapitalize(str)
take the str parameter being passed and capitalize the first letter
of each word. Words will be separated by only one space."
'''

#1 - Identify each substring.
#2 - Capitalize its first character.
#3 - Move to next string.
#Return - Return the edited string.
#Also, this code assumes the string will only be separated by one space,
#though does not assume the string has an apha character in index[0].



def letter_capitalize(string):

    holder_string = ''

    for i in range(len(string)):

        #Capitalize the first letter--if it's a letter
        if i == 0 and string[0].isalpha():
            holder_string +=string[i].upper()

        #Check for space to th left of index[i] and capitalize
        elif string[i-1].isspace() and i > 0 and i < len(string):
            holder_string += string[i].upper()
          
        else:
            holder_string += string[i]

    return holder_string



print letter_capitalize(" every villain is lemons ")

