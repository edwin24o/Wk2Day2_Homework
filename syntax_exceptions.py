#from helper import d

# in Python ther are only two types of issues that will break your code
#-- stop your code from funcioning or executing and throw an error

# Syntax Errors : errors in your coding granmmar, a structural error
#-- misspelling
#-- indentation error
#-- code structure is missing something
#-- colons, indentation, paranthesis, ' ', " " 

# Exceptions : arise when our code is structured correctly but some operation doesn't execute for a variety of reasons

#-- ZeroDivisionError : occurs when you try to divide by 0
# quotient = 10/10

#---- NameError : trying to call a variable or function before its defined
#print(x)
#print(divi())
#def divi():
#    pass

#--- ValueError : trying perform operations with invalid values

#str_num = 'nine'
#int_num = int(str_num)    # trying to conver an invalid value

#--- TypeError : trying to perform opertations no values of inappropriate types 

#num = 5
#total_people = num + "people" # cannot concatenante a str and an int together

#--- AtrributeError : trying to use methonds on improper objects

#word = "Hello"
#word.append("there")

word = "Hello"
rword = word.reversed()
