import pickle

class Animal:
    def __init__(self, number_of_paws, color):
        self.number_of_paws = number_of_paws
        self.color = color

class Sheep(Animal):
    def __init__(self, color):
        Animal.__init__(self, 4, color)

mary = Sheep("white")

print (str.format("My sheep mary is {0} and has {1} paws", mary.color, mary.number_of_paws))
my_pickled_mary = pickle.dumps(mary)

binary_file = open('my_pickled_mary.bin', mode='wb')
my_pickled_mary = pickle.dump(mary, binary_file)
binary_file.close()