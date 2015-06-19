'''
From Coderbyte: "Using the Python language, have the function LetterChanges(str)
take the str parameter being passed and modify it using the following algorithm.
Replace every letter in the string with the letter following it in the alphabet
(ie. c becomes d, z becomes a). Then capitalize every vowel in this new string
(a, e, i, o, u) and finally return this modified string."
'''
#There are two major transformations to str. 
#1-Replace each letter in the string with the letter after it.
#2-Capitalize each vowel.
#Return - Return the finished string.

#NOTE: Since this was CoderByte, I thought the rules were not to
#use any imported modules, even built-in modules. So the solution is
#verbose because of this, though there are probably much better ways
#even with this limitation.

def letter_changes(str):
    #Bad name for a list!
    return_string = []
    final_string = ''
    
    #Shift all letters one letter "to the right." Lowercased everything.
    for i in range(len(str)):
        if str[i] == 'a' or str[i] == 'A':
            return_string.append('b')
        elif str[i] == 'b' or str[i] == 'B':
            return_string.append('c')
        elif str[i] == 'c' or str[i] == 'C':
            return_string.append('d')
        elif str[i] == 'd' or str[i] == 'D':
            return_string.append('e')
        elif str[i] == 'e' or str[i] == 'E':
            return_string.append('f')
        elif str[i] == 'f' or str[i] == 'F':
            return_string.append('g')
        elif str[i] == 'g' or str[i] == 'G':
            return_string.append('h')
        elif str[i] == 'h' or str[i] == 'H':
            return_string.append('i')
        elif str[i] == 'i' or str[i] == 'I':
            return_string.append('j')
        elif str[i] == 'j' or str[i] == 'J':
            return_string.append('k')
        elif str[i] == 'k' or str[i] == 'K':
            return_string.append('l')
        elif str[i] == 'l' or str[i] == 'L':
            return_string.append('m')
        elif str[i] == 'm' or str[i] == 'M':
            return_string.append('n')
        elif str[i] == 'n' or str[i] == 'N':
            return_string.append('o')
        elif str[i] == 'o' or str[i] == 'O':
            return_string.append('p')
        elif str[i] == 'p' or str[i] == 'P':
            return_string.append('q')
        elif str[i] == 'q' or str[i] == 'Q':
            return_string.append('r')
        elif str[i] == 'r' or str[i] == 'R':
            return_string.append('s')
        elif str[i] == 's' or str[i] == 'S':
            return_string.append('t')
        elif str[i] == 't' or str[i] == 'T':
            return_string.append('u')
        elif str[i] == 'u' or str[i] == 'U':
            return_string.append('v')
        elif str[i] == 'v' or str[i] == 'V':
            return_string.append('w')
        elif str[i] == 'w' or str[i] == 'W':
            return_string.append('x')
        elif str[i] == 'x' or str[i] == 'X':
            return_string.append('y')
        elif str[i] == 'y' or str[i] == 'Y':
            return_string.append('z')
        elif str[i] == 'z' or str[i] == 'Z':
            return_string.append('a')
        else:
            return_string.append(str[i])
            
    #Now replace lowercase vowels with uppercase vowels. 
    for i in range(len(str)):
        if return_string[i] == 'a':
            return_string[i] = 'A'
        elif return_string[i] == 'e':
            return_string[i] = 'E'
        elif return_string[i] == 'i':
            return_string[i] = 'I'
        elif return_string[i] == 'o':
            return_string[i] = 'O'
        elif return_string[i] == 'u':
            return_string[i] = 'U'


    #Make sure it outputs as a string, so convert from the list.
    for i in return_string:
        final_string = final_string + i
    
              
    return final_string
        


print letter_changes("AAAbzbbbzc!!cczeeee")


