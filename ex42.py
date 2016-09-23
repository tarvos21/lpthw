## Animal is-a object (yes, sort of confusing) book at the extra credit
class Animal(object):
    pass

## class Dog is-a Animal and has-a __init__ function that takes self, name parameters
class Dog(Animal):

    def __init__(self, name):
        ## class Dog has-a attribute named name and set to name
        self.name = name

## class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## class Cat has-a attribute named name and set to name
        self.name = name

## class Person is-a object
class Person(object):

    def __init__(self, name, salary):
        ## class Person has-a attribute named name and set to name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## class Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## class Employee has-a attribute named salary and set to salary
        self.salary = salary

## class Fish is-a object
class Fish(object):
    pass

## class Salmon is-a Fish
class Salmon(Fish):
    pass

## class Halibut is-a Fish
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

## satan is-s Cat, name set to "Saten"
satan = Cat("Satan")

## mary is-a Person, name set to "Mary"
mary = Person("Mary")

## mary has-a pet of cat kind, named set to Satan
mary.pet = satan

## frank is-a Employee, and has-a salary of 120000, huge!
frank = Employee("Frank", 120000)

## frank has-a pet of dog kind, name set to Rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
