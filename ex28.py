a1 = "True and True"
a2 = "False and True"
a3 = "1 == 1 and 2 == 1"
a4 = '"test" == "test"'
a5 = "1 == 1 or 2 != 1"
a6 = "True and 1 == 1"
a7 = "False and 0 != 0"
a8 = "True or 1 == 1"
a9 = '"test" == "testing"'
a10 = "1 != 0 and 2 == 1"
a11 = '"test" != "testing"'
a12 = '"test" == 1'
a13 = "not (True and False)"
a14 = "not (1 == 1 and 0 != 1)"
a15 = "not (10 == 1 or 1000 == 1000)"
a16 = "not (1 != 10 or 3 == 4)"
a17 = 'not ("tesint" == "testing" and "DuBing" == "Cool Gue")'
a18 = '1 == 1 and (not ("testing" == 1 or 1 == 0))'
a19 = '"chunky" == "bacon" and (not (3 == 4 or 3 == 3))'
a20 = '3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))'

for i in range(1, 21):
    name = eval("a" + str(i))
    print name + ":", eval(name)
