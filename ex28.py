a1 = "True and True"
a2 = "False and True"
a3 = "1 == 1 and 2 == 1"

for i in range(1,4):
    name = "a" + i
    print name
    print name + ":", eval(name)
