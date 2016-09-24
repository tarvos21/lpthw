class Parent(object):

    def override(self):
        print "PARENT override() function is here!"

    def implicit(self):
        print "PARENT implicit() function is here!"

    def altered(self):
        print "PARENT altered() function is here!"

class Child(Parent):

    def override(self):
        print "This is CHILD override() function, great!"

    def altered(self):
        print "This is CHILD altered() function, before PARENT altered() called by super."
        super(Child, self).altered()
        print "This is CHILD altered() function, after PARENT altered() called by super."


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
