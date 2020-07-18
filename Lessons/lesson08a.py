# Curso em Vídeo Lesson 08
# https://www.youtube.com/watch?v=oOUyhGNib2Q&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=24

# Importing the whole library
import math

num = int(input('Type an integer: '))
root = math.sqrt(num)
print('The root of the number {} is {}'.format(num, root))


# Rounding the root

# ceil() rounds up
print('The rounded up root is {}'.format((math.ceil(root))))

# floor() rounds down
print('The rounded down root is {}'.format(math.floor(root)))


# Importing specifics modules from math library
from math import sqrt, ceil, floor

print('- - -')
print('Imported sqrt, ceil and floor from math')

# It changes the way to call the functions
root = sqrt(num)
print('The root with specific modules is {}'.format(root))
print('The rounded up root is {}'.format(ceil(root)))
print('The rounded down root is {}'.format(floor(root)))
