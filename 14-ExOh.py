'''
From CoderByte: "Using the Python language, have the function ExOh(str)
take the str parameter being passed and return the string true if there
is an equal number of x's and o's, otherwise return the string false.
Only these two letters will be entered in the string, no punctuation
or numbers. For example: if str is "xooxxxxooxo" then the output
should return false because there are 6 x's and 5 o's."
'''
#1-Take in a string of only x and o characters (assuming away data entry error).
#2-Count the number of x and o characters.
#3-Return - If there is an equal number, return "true" else return "false"


def ExOh (string):
    x_count = 0
    y_count = 0

    for i in string:
        if i == 'x':
            x_count += 1
        if i == 'o':
            y_count += 1
    if x_count == y_count:
        return "true"
    if x_count != y_count:
        return "false"

print ExOh("xooxxxxooxo")
