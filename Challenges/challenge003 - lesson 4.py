# Challenge 03 - Lesson 04
# Sum of two numbers

print('Sum of two numbers')
num1 = input('Type the first name ')
num2 = input('And the second? ')
su = num1 + num2
print(su)
print('What happened?')


# after prof. explanation on lesson 06.
n1 = int(input('What is the first number? '))
n2 = int(input('What is the second number? '))
s = n1 + n2
print('The sum of {0} and {1} is {2}'.format(n1, n2, s))

# first try was concatenating string, not summing them up,
# need to convert the input to integer: int(input()).
