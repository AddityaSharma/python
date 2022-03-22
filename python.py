# lecture-1: installing python on local machine and running python code in interactive shell (command prompt)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# lecture-2: strings

#creating multiline strings:
s1 = '''my name is
Additya Sharma.'''
print(s1)

s2 = """my name is
Additya Sharma."""
print(s2)


# in-build functions in strings:
message = "Hello World!"
print(message[2]) # O/P : l -> accesing element by index.
print(message[0:7]) # O/P : 'Hello W' -> accesing substring from a string -> [start_point : end_point)
print(message[:9]) # O/P : 'Hello Wor' -> accesing substring from a string -> [ : end_point) -> 0 considered as start_point by default.
print(message[3:]) # O/P : 'lo World!' -> accesing substring from a string -> [start_point : ) -> last possible index considered as end_point by default.
print(len(message)) # length of string message.
print(message.upper()) # convert string message to upper_case.
print(message.lower()) # convert string message to lower_case.
print(message.count('l')) # O/P : 3 -> print number of occurances of 'l' in string 'Hello world!'
print(message.find('l')) # O/P : 2 -> print index of first occurance of 'l' in string 'Hello world!'
print(message.replace('World', 'Universe')) # O/P : 'Hello Universe!' -> replace all occurances of 'World' in string message to 'Universe'


# concatenation of strings:
greeting = 'hello'
name = 'Additya'

# Method - 1: using '+' operator.
s1 = greeting + ', ' + name
print(s1)

# Method - 2: using 'format' method 
s2 = '{}, {}'.format(greeting, name)
print(s2)

# Method - 3: using f-string
s3 = f'{greeting}, {name}'
print(s3)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- #



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# lecture-6: booleans and conditionsals

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

# to get the memory location of an element , we use the id method
a = 7
print(id(a)) -> print outs address of object a.

# is Vs ==
a = [1,2,3]
b = [1,2,3]
print(a == b) # true -> as both list cantains same elements.
print(a is b) # false -> is operators check whether a and b are same objects in memory or not.

c = [4,5,6]
d = c
print(c == d) # true -> as both list cantains same elements.
print(c is d) # true -> both the list share same memory address if we assign one list to another. *important*/

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# lecture-7: Loops and iterations

# for loop:
nums = [1,2,3,4,5]

# kind of for_each loop in c++
for x in nums:
    print(x)

# range -> [0, 10)
for i in range(10):  # single argument specifies the end point(exclusive)
    print(i)

# range -> [1, 11)
for i in range(1, 11):  # first argument specifes the start point(inclusive), second argument the end point(exclusive)
    print(i)


# while loop:
x = 0
while x < 10:
    print(x)
    x += 1
    
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# lecture-8: Functions

# Functions say to stay DRY -> i.e don't repeat yourself.

# declaring an function and leaving it empty for now -> use pass statement to avoid compliation errors
def hello(): 
    pass

# declaring and defining a function
def hello(): 
    print('hello World')

hello() # executing function -> hello world

# declaring and defining a function with return statement
def hello(): 
    return 'hello World'

print(hello()) # executing function

# declaring and defining a function having arguments
def hello(greeting): 
    return '{} World'.format(greeting) # f'{greeting} world' -> same string using f format.

print(hello('Hi')) # executing function


# a bit-advanced topic:
# *args amd **kwargs allow us to accept an arbitrary number of positional and keyword arguments respectively
def student_info(*args, **kwargs):
    print(args) # {'Math', 'Art'} -> its basically a tuple with all our positional arguments
    print(kwargs) # {'name': 'John', 'age': 22} -> its basically a dictionary with all our keyword arguments

student_info('Math', "Art", name='John', age=22)

# another way of sending arguments
def student_info(*args, **kwargs):
    print(args) # {'Math', 'Art'} -> its basically a tuple with all our positional arguments
    print(kwargs) # {'name': 'John', 'age': 22} -> its basically a dictionary with all our keyword arguments

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info) # we have sent a list as args and a dictionary as kwargs using the stated syntax.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# lecture-9: Import Modules and Exploring the standard library

# when we import a complete module, we have all the code from the imported file including any print statements or variable.
# while performing imports of function or variable, we have acess to only those methods or variables that we have imported.

# my_module.py file: -> this file is in the same directory as python.py and will be imported by python.py.
print('Imported my_module...')
test = 'Test String'

def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1


# Importing a complete module 'my_module' in python.py file.
# python.py file :
import my_module # another way of importing to make module name shorter -> import my_module as mm, 'mm' -> new shorter name to my_module.

courses = ['History', 'Math', 'Physics', 'CompSci']
index = my_module.find_index(courses, 'Math') # O/P : 1 -> calling imported function : module_name.function_name().
# index = mm.find_index(courses, 'Math) -> 'mm' refers to my_module.
print(index)


# Importing a function or variable from module 'my_module' in python.py file.
# python.py file :
from my_module import find_index, test # from module_name import function_name/ variable_name.
# another way of importing a function or variable by changing name -> fron my_module import find_index as f_i
courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math') # O/P : 1 -> calling imported function : function_name().
# index = f_i(courses, 'Math) -> 'mm' refers to my_module.
print(index)


# importing files from different directory -> haven't coded it up, used system environment -> explained in lecture -> watch recording.

#importing modules from standard library:
#import module_name;

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- #
