class Other(object):

    def override(self):
        print "OTHER override() method"

    def implicit(self):
        print "OTHER implicit() method"

    def altered(self):
        print "OTHER altered() method"


class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

#    def override(self):
#        self.other.override()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD altered() method, before Other altered() method."
        self.other.altered()
        print "CHILD altered() method, after Other altered() method."


son = Child()

son.implicit()
son.override()
son.altered()
