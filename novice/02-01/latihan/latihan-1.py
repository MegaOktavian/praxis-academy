list(map(int, ["1", "2", "3"]))


def hello_world(h):
    def world(w):
        print(h, w)
        return world # returning functions

h = hello_world # assigning
x = h("hello") # assigning
x

function_list = [h, x]
function_list


# procedural code
starting_number = 96
# get the square of the number
square = starting_number ** 2
# increment the number by 1
increment = square + 1
# cube of the number
cube = increment ** 3
# decrease the cube by 1
decrement = cube - 1
# get the final result
result = print(decrement) # output 783012621312


# define a function `call` where you provide the function and the arguments
def call(x, f):
    return f(x)
# define a function that returns the square
square = lambda x : x*x
# define a function that returns the increment
increment = lambda x : x+1
# define a function that returns the cube
cube = lambda x : x*x*x
# define a function that returns the decrement
decrement = lambda x : x-1
# put all the functions in a list in the order that you want to execute them
funcs = [square, increment, cube, decrement]
# bring it all together. Below is the non functional part. 
# in functional programming you separate the functional and the non functional parts.
from functools import reduce # reduce is in the functools library
print(reduce(call, funcs, 96)) # output 783012621312



# Artikel kedua

def add(a, b):
    return a + b
plus = add
plus(3, 4)  # returns 7


(lambda a, b: a + b)(3, 4)  # returns 7
addition = lambda a, b: a + b
addition(3, 4)  # returns 7

authors = ['Octavia Butler', 'Isaac Asimov', 'Neal Stephenson', 'Margaret Atwood', 'Usula K Le Guin', 'Ray Bradbury']
sorted(authors, key=len)  # Returns list ordered by length of author name
sorted(authors, key=lambda name: name.split()[-1])  # Returns list ordered alphabetically by last name.


val = [1, 2, 3, 4, 5, 6]
# Multiply every item by two
list(map(lambda x: x * 2, val)) # [2, 4, 6, 8, 10, 12]
# Take the factorial by multiplying the value so far to the next item
reduce(lambda: x, y: x * y, val, 1) # 1 * 1 * 2 * 3 * 4 * 5 * 6


def add_bar(items=[]):
    items.append('bar')
    return items
l = add_bar()  # l is ['bar']
l.append('foo')
add_bar() # returns ['bar', 'foo', 'bar']

class Bus(object):
     passengers = set()
     def add_passenger(self, person):
        self.passengers.add(person)

bus1 = Bus()
bus2 = Bus()
bus1.add_passenger('abe')
bus2.add_passenger('bertha')
bus1.passengers  # returns ['abe', 'bertha']
bus2.passengers  # also ['abe', 'bertha']



# Artikel 3

def multiply_2_pure(numbers):
    new_numbers = []
    for n in numbers:
        new_numbers.append(n * 2)
    return new_numbers

original_numbers = [1, 3, 5, 10]
changed_numbers = multiply_2_pure(original_numbers)
print(original_numbers) # [1, 3, 5, 10]
print(changed_numbers)  # [2, 6, 10, 20]


mutable_collection = ['Tim', 10, [4, 5]]
immutable_collection = ('Tim', 10, [4, 5])
# Reading from data types are essentially the same:
print(mutable_collection[2])    # [4, 5]
print(immutable_collection[2])  # [4, 5]
# Let's change the 2nd value from 10 to 15
mutable_collection[1] = 15
# This fails with the tuple
immutable_collection[1] = 15


mutable_collection = ['Tim', 10, [4, 5]]
immutable_collection = ('Tim', 10, [4, 5])
immutable_collection[2].append(6)
print(mutable_collection[2])    # [4, 5]
print(immutable_collection[2])  # [4, 5, 6]


def write_repeat(message, n):
    for i in range(n):
        print(message)
write_repeat('Hello', 5)


def hof_write_repeat(message, n, action):
    for i in range(n):
        action(message)

hof_write_repeat('Hello', 5, print)

# Import the logging library
import logging
# Log the output as an error instead
hof_write_repeat('Hello', 5, logging.error)

def add2(numbers):
    new_numbers = []
    for n in numbers:
        new_numbers.append(n + 2)
    return new_numbers
print(add2([23, 88])) # [25, 90]


def hof_add(increment):
    # Create a function that loops and adds the increment
    def add_increment(numbers):
        new_numbers = []
        for n in numbers:
            new_numbers.append(n + increment)
        return new_numbers
    # We return the function as we do any other value
    return add_increment
add5 = hof_add(5)
print(add5([23, 88]))   # [28, 93]
add10 = hof_add(10)
print(add10([23, 88]))  # [33, 98]

def hof_product(multiplier):
    return lambda x: x * multiplier
mult6 = hof_product(6)
print(mult6(6)) # 36


names = ['Shivani', 'Jason', 'Yusef', 'Sakura']
greeted_names = map(lambda x: 'Hi ' + x, names)
# This prints something similar to: <map object at 0x10ed93cc0>
print(greeted_names)
# Recall, that map returns an iterator 
# We can print all names in a for loop
for name in greeted_names:
    print(name)


numbers = [13, 4, 18, 35]
div_by_5 = filter(lambda num: num % 5 == 0, numbers)
# We can convert the iterator into a list
print(list(div_by_5)) # [35]


# Let's arbitrarily get the all numbers divisible by 3 between 1 and 20 and cube them
arbitrary_numbers = map(lambda num: num ** 3, filter(lambda num: num % 3 == 0, range(1, 21)))
print(list(arbitrary_numbers)) # [27, 216, 729, 1728, 3375, 5832]


# Recall
names = ['Shivani', 'Jan', 'Yusef', 'Sakura']
# Instead of: map(lambda x: 'Hi ' + x, names), we can do
greeted_names = ['Hi ' + name for name in names]
print(greeted_names) # ['Hi Shivani', 'Hi Jason', 'Hi Yusef', 'Hi Sakura']


# Recall
numbers = [13, 4, 18, 35]
# Instead of: filter(lambda num: num % 5 == 0, numbers), we can do
div_by_5 = [num for num in numbers if num % 5 == 0]

print(div_by_5) # [35]

# We can manage the combined case as well:
# Instead of: 
# map(lambda num: num ** 3, filter(lambda num: num % 3 == 0, range(1, 21)))
arbitrary_numbers = [num ** 3 for num in range(1, 21) if num % 3 == 0]
print(arbitrary_numbers) # [27, 216, 729, 1728, 3375, 5832]

