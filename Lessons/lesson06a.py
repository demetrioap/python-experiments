# Curso em Vídeo Lesson 06
# Primitive Types and Data Output
# https://www.youtube.com/watch?v=hdDHg1p3YVc&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=9

n1 = int(input('Type the first number: '))
n2 = int(input('Type the second number: '))
s = n1 + n2

# regular print.
print('Result is', s)

# print using format().
print('The sum is {}'.format(s))


# Finding the type using type()

n1 = int(input('Type a number: '))
print('The type of the number is:')
print(type(n1))

n2 = int(input('Type another number '))
print(type(n2))

s = n1 + n2

print('Result is: {}'.format(s))

# Output options

# my way before teacher's resolution.
print('The sum of {}'.format(n1) + ' and {}'.format(n2) + ' is: {}'.format(s))

# teacher's solution.
print('The sum of {} and {} is {}'.format(n1, n2, s))

# another option, printing via index.
print('The sum of {0} and {1} is {2}'.format(n1, n2, s))
