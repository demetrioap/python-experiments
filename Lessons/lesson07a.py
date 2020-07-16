# Curso em Vídeo Lesson 06
# https://www.youtube.com/watch?v=Vw6gLypRKmY&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=12

# name = str(input('What is your name? '))
name = 'Yoyo'  # só pra teste
print('Nice to meet you, {:20}!'.format(name))  # alignment

print('Hi, {:>20}!'.format(name))  # right aligned

print('Hello, {:<20}!'.format(name))  # left aligned

print('Hello, {:^20}!'.format(name))  # centralized

print('Hello, {:=^20}!'.format(name))  # fancy centralized, other characters may be used in place of "="


# calculating inside format()

n1 = int(input('Type a value: '))
n2 = int(input('Type another value: '))
print('The sum is {}'.format(n1 + n2))


# a few operations

s = n1 + n2
m = n1 * n2
d = n1 / n2
integer_division = n1 // n2
e = n1 ** n2
print('The sum is {}, the product is {}, and the division is {:.3f}'.format(s, m, d))  # :.3f for three decimal spaces
print('The integer division is {} and the power is {}'.format(integer_division, e))


# other ways to print

print('-- ' * 10)
print('The sum is {}, \n the product is {}, \n and the division is {:.3f}'.format(s, m, d), end=' ')
print('The integer division is {} and the power is {}'.format(integer_division, e))


# it is possible to put character on "end"

print('-- ' * 10)
print('The sum is {}, the product is {} and the division is {:.3f}'.format(s, m, d), end=' >>> ')
print('The integer division is {} and the power is {}'.format(integer_division, e))
