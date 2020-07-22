# Curso em Vídeo Lesson 10
# Conditions
# https://www.youtube.com/watch?v=K10u3XIf1-Q&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=38

time = int(input('Car''s age: ').strip())

if time <= 3:
    print('Car is new')
else:
    print('Car is old')
print('-- END --')


# Another way, using things that I remembered
# less prints

if time <= 3:
    sentence = 'car is new'
else:
    sentence = 'car is old'
print(sentence)
print('- end -')


# Using simplified condition, one line

print('car is new' if time <= 3 else 'car is old')
print('-- END --')


# More examples

name = str(input('Type a name: ').strip())
if name == 'Cutie':
    print('Aren''t you beutiful? :9')
print('Hello, {}!'.format(name))
