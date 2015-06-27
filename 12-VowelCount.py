'''
From CoderByte: "Using the Python language, have the function VowelCount(str)
take the str string parameter being passed and return the number of vowels
the string contains (ie. "All cows eat grass" would return 5). Do not count
y as a vowel for this challenge."
'''
#1-Take in a string
#2-Iterate over the string and search for vowels
#3-Lowercase each string[i] character so it only needs to look for lowercase vowels
#Return the number of vowels found

def vowel_count(string):
    count = 0
    for i in range(len(string)):
        if string[i].lower() in "aeiou":
            count += 1

    return count


print vowel_count("All cows eat grass")
