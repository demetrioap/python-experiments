# Curso em Vídeo Lesson 06b
# Primitives Types and Data Output
# https://www.youtube.com/watch?v=hdDHg1p3YVc&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=9

n = input('Type something: ')

print('The type is')
print(type(n))

print('Is it numeric?')
print(n.isnumeric())

print('Is it made by letters?')
print(n.isalpha())

print('Is it alphanumeric?')
print(n.isalnum())

print('Is it in CAPS?')
print(n.isupper())

# always "True" if input is provided.
print('Is it True or False?')
print(bool(n))
