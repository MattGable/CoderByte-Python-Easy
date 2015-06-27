'''
From CoderByte: Using the Python language, have the function ABCheck(str)
take the str parameter being passed and return the string true if the
characters a and b are separated by exactly 3 places anywhere in the
string at least once (ie. "lane borrowed" would result in true because
there is exactly three characters between a and b). Otherwise return
the string false. 
'''
#1-Take string input and...
#2-for every 'a' or 'b'. find out if there is a 'b' or 'a' respectively at [i+4]
#Return "true" if so, else return "false"

def ABCheck(string):

    for i in range(len(string)):
        #len(string)-4 used to keep the loop from looking out of range
        if i < len(string)-4 and string[i] == 'a' and string[i+4] == 'b':
            return "true"
        if i < len(string)-4 and string[i] == 'b' and string[i+4] == 'a':
            return "true"
    return "false"

print ABCheck("lane borrowed")


