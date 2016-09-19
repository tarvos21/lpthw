my_name = 'Du Bing'
my_age = 27 # not a lie
my_height = 183 # centimeters
my_weight = 90 # kilograms
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d centimeters tall." % my_height
print "He's %d kilograms heavy." % my_weight
print "Actual that's a little too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the food." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
        my_age, my_height, my_weight, my_age + my_height + my_weight)
