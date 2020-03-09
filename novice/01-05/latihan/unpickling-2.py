import pickle

class my_zen_class:
    number_of_meditations = 0
    def __init__(self, name):
        self.number_of_meditations = 0
        self.name = name

    def meditate(self):
        self.number_of_meditations = self.number_of_meditations + 1
    
    def __getstate__(self):
        # this method is called when you are 
        # going to pickle the class, to know what to pickle

        state = self.__dict__.copy()

        # You will never get the Buddha state if you count 
        # meditations, so 
        # don't pickle this counter, the next time you will just 
        # start meditating from scratch :)
        del state['number_of_meditations']

        return state

    def __setstate__(self, state):
        # this method is called when you are going to 
        # unpickle the class,
        # if you need some initialization after the 
        # unpickling you can do it here.

        self.__dict__.update(state)

# I start meditating
my_zen_object = my_zen_class("Dave")
for i in range(100):
    my_zen_object.meditate()

# Now I pickle my meditation experience
print(str.format("I'm {0}, and I've meditated {1} times'", my_zen_object.name, my_zen_object.number_of_meditations))
my_pickled_zen_object = pickle.dumps(my_zen_object)
my_zen_object = None

# Now I get my meditation experience back
my_new_zen_object = pickle.loads(my_pickled_zen_object)

# As expected, the number_of_meditations property 
# has not been restored because it hasn't been pickled
print(str.format("I'm {0}, and I don't have a beginner mind yet because I've meditated only {1} times'", my_new_zen_object.name, my_new_zen_object.number_of_meditations))