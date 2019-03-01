""" Parse multiline input and process each line until you come to 
a keyword and assign the rest of the text until end of the string 
to a variable. 

Sample input:
abc
def
keyword
ghi
jkl

output: 
var1 - abc
       def

var2 - ghi
       jkl

bonus: do this with one loop pass

 """
 ##############################
import re

test = """
this is a test
another test
abc
more testing
and more test
"""
body = str()

input = test.splitlines()

for i, line in enumerate(input):
    
    if re.match("abc", line):
        body += str(input[i+1:])
        break

    print(line) # parse header here

print("HERE:", body)