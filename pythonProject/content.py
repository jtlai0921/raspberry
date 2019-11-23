a = 10
a = 10
c = 10
b = 20
if a < b:
    print("Hello!")
else:
    print("world")

empty_tuple = ()
empty_tuple
()
one_marx = 'Groucho',
one_marx
('Groucho',)
marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_typle
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'marx_typle' is not defined
marx_tuple
('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
a
'Groucho'
b
'Chico'
c
'Harpo'
'''
empty_dict = {}
empty_dict
{}
lol = {1:'one', 2:'two'}
lol
{1: 'one', 2: 'two'}

'''

disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")

Woe!


color = "puce"
if color == "red":
    print("it's a tomato")
elif color == "green":
    print("it's a green pepper")
elif color == "bee purple":
    print("only bees")
else:
    print("another")

another
x = 7
x == 5
False
x == 7
True
5 < x
True
x < 10
True
5 < x and x < 10
True
x < 5 and x < 10
False
5 < x or x < 10
True
x < 5 or x < 10
True
5 < x and not x > 10
True


while True:
    stuff = input("String to capitalize type q to quit:")
    if stuff == 'q':
        break;
    print(stuff.capitalize())

 while True:
...     value = input("Integer, please [q to quit]:")
...     if value == 'q':
...             break
...     number = int(value)
...     if number % 2 == 0:
...             continue
...     print(number, "squared is", number*number)