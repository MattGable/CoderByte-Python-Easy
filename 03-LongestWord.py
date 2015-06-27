'''
From CoderByte: "Using the Python language, have the function LongestWord(sen)
take the sen parameter being passed and return
the largest word in the string. If there are two or
more words that are the same length, return the first
word from the string with that length. Ignore punctuation
and assume sen will not be empty."
'''

#Iterate over a string and find the
#longest unbroken string of letter characters.
#This program does not report a tie and returns the
#first longest string (per the rules).

def longest_word(sen):
    word_final = ''
    word_holder = ''

    for i in sen:
        
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            word_holder = word_holder + i

            if len(word_final) < len(word_holder):
                word_final = word_holder
                
        if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            word_holder = ''
            
    return str(word_final)


print longest_word("ha!Yyy!zzzzhhh dianubd jjkbfyuoauisvfyrui")









