class Parent(object):

    def implicit(self):
        print "PARENT implicit()"


class Child(Parent):
    pass

dad = Parent()
son = Child()

son.implicit()
dad.implicit()
