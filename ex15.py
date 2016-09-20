from sys import argv

# get script name and target filename
script, filename = argv

# open the target file with builtin function 'open'
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()    # print the content with builtin function 'read'

txt.close()    # close the file

print "Type the filename again:"
file_again = raw_input(">>> ")    # get the filename from user

txt_again = open(file_again)

print txt_again.read()
