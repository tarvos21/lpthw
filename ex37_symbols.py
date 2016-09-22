***Keywords***
and    Logical and.    True and False == False
as    Part of the with-as statment.    with X as Y: pass
assert    Assert(ensure) that something is true.    assert False. "Error!"
break    Stop this loop right now.    while True: break
class    Define a class.    class Person(object)
continue   Do not process more of the loop, do it again.    while True: continue
def    Define a function.    def X(): pass
del    Delete from dictionary.    def X[Y]
elif    Else if condition.    if: X; elif: Y; else: J
else    Else condition.    if: X; elif: Y; else: J
except    If and exception happens, do this.    except ValueError. e: print e
exec    Run a string as Python.    exec 'Print "hello"'
finally    Exceptions or not, finally do this no matter what.    finally: pass
for   Loop over a collection of things.    for X in Y: pass
from    Importing specific parts of a module.    from X import Y
global    Declare that you want a global variable.    global X
if    If condition.    if: X; elif: Y; else: J
import    Import a module into this one to use.    import os
in    Part of for-loops. Also a test of X in Y.    for X in Y: pass also 1 in [1] == True
is    Like == to test equality.    1 is 1 == True
lambda    Create a short anonymous function.   s = lambda v: v ** y; s(3)
not     Logical not.    not True == False
or    Logical or.    True or False == True
pass    This block is empty.    def empty(): pass
print    Print this string.    print 'this string'
raise    Raise an exception when things go wrong.    raise ValueError("No")
return    Exit the funtion with a return value.    def X(): return Y
try    Try this bolck, and if exception, go t oexcept.    try: pass
while    While loop.    while X: pass
with    With an expression as a variable do.    with X as Y: pass
yield    Pause here and return to caller.    def X(): yield Y; X().next()

***Data Types***
True    True boolean value.    True or False == True
False   False boolean value.    False and True == False
None    Represents "nothing" or "no value".    x = None
strings    Stores textual information.    x = "hello"
numbers    Stores integers.    i = 100
floats    Stores decimals.    i = 10.389
lists    Stores a list of things.    i = [1, 2, 3, 4]
dicts    Stores a key=value mapping of things.    e = {'x': 1, 'y': 2}

***String Escape Sequences***
\\    Backslash
\'    Single-quote '
\"    Double-quote "
\a    Bell
\b    Backspace
\f    Formfeed
\n    Newline
\r    Carriage
\t    Tab
\v    Vertical tab

***String Formats***
%d    Decimal integers(not floating point).    "%d" % 45 == '45'
%i    Same as %d.    "%i" % 45 == '45'
%o    Octal number.    "%o" % 1000 == '1750'
%u    Unsigned decimal.    "%u" % -1000 == '-1000'
%x    Hexadecimal lowercase.    "%x" % 1000 == '3e8'
%X    Hexadecimal uppercase.    "%X" % 1000 == '3E8'
%e    Exponential notation, lowercase 'e'.    "%e" % 1000 == '1.000000e+03'
%E    Exponential notation, uppercase 'E'.    "%E" % 1000 == '1.000000E+03'
%f    Floatig point real number.    "%f" % 10.34 == '10.340000'
%F    Same as %f.    "%F" % 10.34 == '10.340000'
%g    Either %f or %e, whichever is shorter.    "%g" % 10.34 == '10.34'
%G    Same as %g but uppercase.    "%G" % 10.34 == '10.34'
%c    Character format.    "%c" % 34 == '"'
%s    String format.    "Hi, %s" % 'DuBing' == 'Hi, DuBing'
%%    A percent sign.    "%g%%" % 10.34 == '10.34%'

***Operators***
+    Addtion    2 + 4 == 6
-    Subtraction    2 - 4 == -2
*    Multiplication    2 * 5 == 10
**    Power of    2 ** 8 == 256
/    Division    2 / 4.0 == 0.5
//    Floor division    2 / 4.0 == 0.0
%    String interpolate or modulus    2 % 4 == 2
<    Less than    3 < 5 == True
>    Greater than    3 > 5 == False
<=    Less than equal    5 <= 3 == False
>=    Greater than equal 7 >= 7 == True
==    Equal    10 == 0 == False
!=    Not equal    4 != 18 == True
<>    Not equal    3 <> 1 == True
()    Parenthesis    len('hi') == 2
[]    List brackets    [1, 3, 4]
{}    /dict curly braces    {'x': 5, 'y': 3}
@    At(decorators)    @classmethod
,    Comma    range(0, 1000)
:    Colon    def X():
.    Dot    self.x = 10
=    Assign equal    x = 10
;    Semi-colon    print "hi"; print "there"
+=    Add and assign    x = 1; x += 2
-=    Subtract and assign    x = 1; x -= 2
*=    Multiply and assign    x = 1; x *= 2
/=    Divide and assign    x = 1; x /= 2
//=    Floor divide and assign    x = 1; x //= 2
%=    Modulus assign    x = 1; x %= 2
**=    Power assign    x = 1; x **= 2
