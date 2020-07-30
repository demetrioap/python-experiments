# Curso em Vídeo Lesson 13
# for loop
# https://www.youtube.com/watch?v=cL4YDtFnCt4&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=13

# prof. calls "c" a "counter"
for c in range(0, 6):
    print('Hi')
print('-= END =-')

# setting to print the value of "c", which is the variable in range between 0 and 6 above,
# it will print from 0 to 5
# because range goes from the first index to before the last.
for c in range(0, 6):
    print(c)
print('-= END of c =-')

# reverse iteration
# range(start, stop[, step]), step is optional
for c in range(109, 0, -1):
    print(c)
print('-= END of reverse =-')

# it is possible to use the "step" parameter to skip by 2
for number in range(0, 10, 2):
    print(number)
print('-= END skipping by 2 =-', end='\n\n')


# With variable via input

# section separator
print('-' * 12 + ' With user input ' + '-' * 12)

n = int(input('Type a number: ').strip())
for n in range(0, n + 1):
    print(n)
print('END with input 1')

# with more input from user
beginning = int(input('Beginning: ').strip())
end = int(input('End: ').strip())
steps = int(input('Steps: ').strip())

for c in range(beginning, end + 1, steps):
    print(c)
print('-= END with more input =-')

# nesting input
for c in range(0, 3):
    n = int(input('Type a value: ').strip())
    print(n)
print('END')
print(n)

# iterating with a variable
print('\n-- Iterating with a variable --')
s = 0
for c in range(0, 4):
    n = int(input('Type a number: ').strip())
    s += n
print('The sum of all typed numbers is {}'.format(s))
print('-= END with sum =-')
