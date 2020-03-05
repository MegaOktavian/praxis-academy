class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return self.name+' says Woof!'
    
class Cat(Animal):
    def speak(self):
        return self.name+' says Meow!'
    
fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())

class Animal:
    def __init__(self,name,legs):
        self.name = name
        self.legs = legs

class Bear(Animal):
    def __init__(self,name,legs=4,hibernate='yes'):
        Animal.__init__(self,name,legs)
        self.hibernate = hibernate
        
yogi = Bear('Yogi')
print(yogi.name)
print(yogi.legs)
print(yogi.hibernate)

class Car:
    def __init__(self,wheels=4):
        self.wheels = wheels
        # We'll say that all cars, no matter their engine, have four wheels by default.

class Gasoline(Car):
    def __init__(self,engine='Gasoline',tank_cap=20):
        Car.__init__(self)
        self.engine = engine
        self.tank_cap = tank_cap # represents fuel tank capacity in gallons
        self.tank = 0
        
    def refuel(self):
        self.tank = self.tank_cap
        
    
class Electric(Car):
    def __init__(self,engine='Electric',kWh_cap=60):
        Car.__init__(self)
        self.engine = engine
        self.kWh_cap = kWh_cap # represents battery capacity in kilowatt-hours
        self.kWh = 0
    
    def recharge(self):
        self.kWh = self.kWh_cap

class Hybrid(Gasoline, Electric):
    def __init__(self,engine='Hybrid',tank_cap=11,kWh_cap=5):
        Gasoline.__init__(self,engine,tank_cap)
        Electric.__init__(self,engine,kWh_cap)
        
        
prius = Hybrid()
print(prius.tank)
print(prius.kWh)

prius.recharge()
print(prius.kWh)

class A:
    num = 4
    
class B(A):
    pass

class C(A):
    num = 5
    
class D(B,C):
    pass

D.num

class A:
    def truth(self):
        return 'All numbers are even'
    
class B(A):
    pass

class C(A):
    def truth(self):
        return 'Some numbers are even'

class D(B,C):
    def truth(self,num):
        if num%2 == 0:
            return A.truth(self)
        else:
            return super().truth()
            
d = D()
d.truth(6)
d.truth(5)