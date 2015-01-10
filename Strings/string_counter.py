# Write a function that takes a piece of text in the form 
# of a string and returns the letter frequency count 
# for the text. This count excludes numbers, spaces and 
# all punctuation marks. Upper and lower case versions of 
# a character are equivalent and the result should all be 
# in lowercase.

# # The function should return a list of tuples sorted by the 
# most frequent letters first. Letters with the same frequency 
# are ordered alphabetically. For example:

#   letter_frequency('aaAabb dddDD hhcc')

from string import ascii_lowercase

def get_freq(instring):
    stringletters = list()
    string_numbers = list()
    for letter in instring:
        if letter.lower() in ascii_lowercase:
            if letter.lower() in stringletters:
                ind = stringletters.index(letter.lower())
                string_numbers[ind] += 1
                #incremenet count
            else:
                stringletters.append(letter.lower())
                string_numbers.append(1)
    d = sorted(list(zip(stringletters, string_numbers)), key = lambda x: x[0])
    return sorted(d, key = lambda x: x[1], reverse = True)

if __name__ == '__main__':

    print(get_freq('aaAabb dddDD hhcc'))