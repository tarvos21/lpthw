def finger_and_eye(finger_count, eye_count):
    print "You have %d fingers!" % finger_count
    print "You have %d eyes!" % eye_count
    print "Man that's enough for a man!"
    print "Get a piss.\n"


print "We can just give the function numbers directly:"
finger_and_eye(9, 3)


print "OR, we can use variables from our script:"
amount_of_finger = 9
amount_of_eye = 2

finger_and_eye(amount_of_finger, amount_of_eye)


print "We can even do math inside too:"
finger_and_eye(7+4, 5-1)


print "And we can combine the two, variables, and math:"
finger_and_eye(amount_of_finger + 120, amount_of_eye ** 100)


def calculate_pmi():
    height = float(raw_input("How tall are you in 'm'? "))
    weight = float(raw_input("How much do you weigh in 'kg'? "))
    pmi = weight/height ** 2
    print "Your PMI is %f." % pmi
    if pmi > 25:
        print "Hi, man, you are over-weighted, try to lose some fat."
    elif pmi < 18:
        print "Hi, man, you are so slim, tell your mom to cook better."
    else:
        print "Hi, man, you body is perfect, keep it, you are great!"

calculate_pmi()
