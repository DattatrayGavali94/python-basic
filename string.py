print(type("hi hello there 24!"))
username = 'supercoder'
password = 'supersecret'

long_string = '''
WOW
O O
---
'''

print(long_string)

# String conctenation

print('hello'+'Dtttry')
# print('hello'+5) # TypeError: can only concatenate str (not "int") to str

# type conversion
print(str(100))
print(type(str(100)))
print(type(int(str(100))))

# Escape Sequence
weather = "\t It\'s \"kind of\" sunny \n hope you have a good day!"
print(weather)

# formatted strings
name = "Johnny"
age = 55

# python 3
print(f'hi {name}. you are {age} years old')

# python 2
print('hi {}. you are {} years old'.format(name,age))
print('hi {1}. you are {0} years old'.format(name,age))
print('hi {new_name}. you are {age} years old'.format(new_name="d",age="2"))

# string index

string1 = 'Dattatray'
         # 012345678
print(string1[0] + string1[1])

# [start:stop:stepover] -> string slicing 
print(string1[0:4:1])
print(string1[::1]) 
print(string1[0:8:2])

# immutability (string value can't be change)


# bulit in funcation + method
print(len("dattatray"))


# booleans
isCool = False

isCool = True

print(bool(1))
print(bool(0))
print(bool('True'))
print(bool('False'))
# Exercise : Type conversion
