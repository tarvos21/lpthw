class Parent(object):

    def altered(self):
        print "PARENT altered() function is here."

class Child(Parent):
    
    def altered(self):
        print "CHILD altered() function here, before PARENT altered()"
        # use a built-in fuction super to call the Parent version of altered()
        super(Child, self).altered()
        print "CHILD, after PARENT altered(), haha, magic super!"

dad = Parent()
son = Child()

dad.altered()
son.altered()
