# Challenge 004 - Lesson 06
# Checking the type of something

something = input('Type something ')
print('You typed "{}" of type {}'.format(something, type(something)))
print('Is it alphanumeric?', something.isalnum())
print('Is it alphabetic?', something.isalpha())
print('Is it numeric?', something.isnumeric())
print('Is it decimal?', something.isdecimal())
print('Is it possible to print to the screen?', something.isprintable())
print('Is it a space?', something.isspace())
print('Is it in Uppercase?', something.isupper())
print('Is it in lowercase?', something.islower())
print('Is it capitalized?', something.istitle())
