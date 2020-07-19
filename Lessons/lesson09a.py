# Curso em Vídeo Lesson 09
# https://www.youtube.com/watch?v=a7DH88vk2Sk&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=31

# Sentence provided by Totz! /o/
sentence = 'Kept you waiting, Huh?'

# Slicing

# first character
print(sentence[0])

# Range goes from the first value up to the value before the second
print(sentence[0:4])

# selecting one after the last value to show the "?" character
# there are 22 characters, index from 0 to 21
print(sentence[0:22])

# skipping by 2
# add :2 to the end
print(sentence[0:22:2])


# start from the beginning and goes to the fourth index
print(sentence[:5])

# start from "you" e goes to the end
# better for when the index of the last character is not known
print(sentence[5:])

# from the 3rd character to the end,
# but skipping 3 characters, counted from the index
print(sentence[2::3])



###

# Analysis

# quantity of characters in the string
print(len(sentence))

# how many "i" there are in the string
print(sentence.count('i'))


# Count with slicing

# from 0 to 12, since 13 won't be in, as above
letter = 'i'
print('There is/are {} letter(s) {} in the sentence, until the marked character'.format(sentence.count(letter, 0, 22), letter))


# first index locator
# or where each word or piece starts
word = 'waiting'
print('First index of word "{}" is: {}'.format(word, sentence.find(word)))

# when it returns -1 it means the string was not found
# therefore, it can be used inside an "if", for example, to warn the string was not located
print(sentence.find('Hein'))


# check if the string exists in the sentence
print('huh' in sentence)

# it differentiates upper from lower cases
# here it will return "False"
print('kept' in sentence)


# Transformation

print('Replace "waiting" for "cooking"')
print(sentence.replace('waiting', 'cooking'))

print('Transforms to UPPER case')
print(sentence.upper())

print('Transforms to lower case')
print(sentence.lower())

# it looks for 'kept' inside the sentence after it is converted to lower case
# the result must be index 0
print(sentence.lower().find('kept'))

# First letter in upper case
print(sentence.capitalize())

# All first letters in upper case
print(sentence.title())


# Strip

# strip removes blank spaces (trailing spaces) from the beginning and from the end of the sentence
sentence_with_space = '  Sentence   Strip  '
strip = sentence_with_space.strip()
print('The sentence {}, without spaces on the sides looks like this: {}.'.format(sentence_with_space, strip))

# rstrip removes spaces from the right side
# there are many functions with 'r' variation
print('The sentence {}, without spaces on the right side: {}.'.format(sentence_with_space, sentence_with_space.rstrip()))

# lstrip removes spaces from the left side
print('The sentence {}, without spaces on the left side: {}.'.format(sentence_with_space, sentence_with_space.lstrip()))


# Division

# takes spaces in consideration
# and resets the index for each word
splitted_sentence = sentence.split()
print('Splitted sentence')
print(splitted_sentence)

# showing only the second string from the list after the split
print('The second string from the splitted sentence')
print(splitted_sentence[1])

# showing the third letter inside the second string after split
print('The 3rd letter inside the 2nd string after split')
print(splitted_sentence[1][2])


# String Join

print('-'.join(splitted_sentence))

print('-'.join(['banana', 'melon']))
