# -------- First-Class Functions --------

def greeting():
    print('Hello World !')

greeting()

# atau

def greeting():
    print('Hello World !')

greeting()
greeting.lang = 'English'
greeting.lang


# -------- Assigning Functions to Variables --------

square = lambda x : x*x
square(5)

# atau menggunakan fungsi

def square(x):
    return lambda x: x * x

x = square(5)
print(x(5))

foo = square(6)
print(foo(6))


# -------- Passing Functions as Parameters --------

def formalGreeting():
    print('How are you?')

def casualGreeting():
    print("What's up?")

def greet(type):
    if(type == 'formal'):
        formalGreeting()
    elif(type == 'casual'):
        casualGreeting()

greet('casual')

# -------- Higher-Order Functions : Array.prototype.map --------
# tanpa Higher-Order Functions contoh 1

arr1 = [1,2,3]
arr2 = []

for i in range(len(arr1)):
    arr2.append(arr1[i]*2)

arr2

# menggunakan Higher-Order Functions contoh 1

def arr2(arr1):
    nomor  = []
    for i in range(len(arr1)):
        nomor.append(arr1[i]*2)
    return nomor

print(arr2([1,2,3]))

# tanpa Higher-Order Functions contoh 2

birthYear = [1975, 1997, 2002, 1995, 1985]
ages = []

for i in range(len(birthYear)):
    ages.append(2018 - birthYear[i])

ages

# menggunakan Higher-Order Functions contoh 2


def ages(birthYear):
    umur = []
    for i in range(len(birthYear)):
         umur.append(2018 - birthYear[i])
    return umur

print(ages([1975, 1997, 2002, 1995, 1985]))


# -------- Higher-Order Functions : Array.prototype.filter --------
# tanpa Higher-Order Functions contoh 1

persons = [
    { 'name' : 'Peter', 'age' : 16 },
    { 'name' : 'Mark', 'age' : 18 },
    { 'name' : 'John', 'age' : 27 },
    { 'name' : 'Jane', 'age' : 14 },
    { 'name' : 'Tony', 'age' : 24 }
]

print(persons[int('1')].get('age'))
fullAge = []
for i in range(len(persons)):
    a = persons[i].get("age")
    if a >= 18:
        fullAge.append(persons[i])
    elif a < 18:
        print("Data tidak ada")
fullAge

# -------- Higher-Order Functions : Array.prototype.reduce --------
# tanpa Higher-Order Functions contoh 1

arr = [5, 7, 1, 8, 4]
jumlah = 0
def sum(arr):
    global jumlah
    for i in range(len(arr)):
        jumlah = jumlah + int(arr[i])
    return jumlah
jumlah = sum(arr)
jumlah


# menggunakan Higher-Order Functions contoh 1

arr = [5, 7, 1, 8, 4]
sum = 0

for i in range(len(arr)):
    sum = sum + int(arr[i])

sum


# -------- Creating Our own Higher-Order Function --------

strArray = ['JavaScript', 'Python', 'PHP', 'Java', 'C']

def kata(strArray):
    panjang = []
    for i in range(len(strArray)):
        panjang.append(len(strArray[i]))
    return panjang

total = kata(strArray)
total