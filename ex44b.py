class Parent(object):

    def override(self):
        print "PARENT override()"
        print "This is override function in Parent class."


class Child(Parent):

    def override(self):
        print "CHILD override()"
        print "This is override funciton in Child class."
        print "The override function in Child class is stronger,"
        print "killing the Parent override function."
        

dad = Parent()
son = Child()

dad.override()
son.override()
