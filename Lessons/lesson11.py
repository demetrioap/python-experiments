# Curso em Vídeo Lesson 11
# Colors on Terminal
# https://www.youtube.com/watch?v=0hBIhkcA8O8&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=47

# print('\033[0;30;41mTest')
#
# print('\033[4;33;44mTest')
#
# print('\033[1;35;43mTest')

# \033[30;42m

# \033[m - can be used to undo the color configuration

# \033[7;30m

print('\033[1;31;43mHello, World!\033[m')

a = 3
b = 5

print('The values are \033[32m{}\033[m and \033[31m{}\033[m!!!'.format(a, b))

# using inside .format()
name = 'Ichigo'
print('Hi, {}{}{}!'.format('\033[4;36m', name, '\033[m'))

# using dictionary (that prof explains in another lesson)
colors = {'clear': '\033[m',
         'blue': '\033[34m',
         'yellow': '\033[33m',
         'black-and-white': '\033[7;30m'}

print('Hello, {}{}{}!'.format(colors['black-and-white'], name, colors['clear']))
