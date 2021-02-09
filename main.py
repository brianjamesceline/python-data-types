'''
Text Type (String)
'''

# s = 'This is a single string'
# print(s)
# print(type(s))

#======================================

# s = """this is a multiline string 
# example"""
# print(s)

#======================================

# # find a character by index
# s = 'string sample'
# print(s[5])

# slicing
# s = 'string sample'
# print(s[0:6])

#======================================
#immutable (Cannot change the string value)

# s = 'string sample'
# s[2] = 'o')
# print(s)

'''
Numeric Type (Integer, Float, Complex)
'''
# x = 1234567890
# print(type(x))

# float is accurate up to 15-16 decimal places
# x = 0.123456789012345678912345
# print(type(x))


# x = 1+2j
# print(type(x))

'''
Sequence Type (List, Range)
'''
#homogeneous
# x = []
#list
# x = [10,2.5,'hello']
# print(x[1])
# print(x[1:3])

# # mutable (lists are mutable)
# x[2] = 'Python'
# print(x)

#Tuple
# Heterogeneous
# tuple = ()

#======================================

# both of below examples are type tuples, without the comma makes them a string.
# tuple = ("hello",)
# tuple = "hello",
# print(type(tuple))

#======================================

# tuple = ("cat", [4,3,2], (1,2,3))
# print(tuple[2])

#======================================

# immutable

# tuple = ("cat", [4,3,2], (1,2,3))
# tuple[2] = 10
# print(tuple)

#======================================

# range

# x = range(10)
# for n in x:
#   print(n)

'''
Mapping Type (Dictionary)
'''
# dict = {}
# print(type(dict))

#======================================
# dict is mutable
# dict = {'name': 'Kingsley', 'age':37}
# print(dict['age'])
# print(dict.get('name'))

# dict['age'] = 26
# print(dict)

'''
Set Types
'''
#set = {} #This is a Dictionary when empty
# set = set() # This is a set

# set = {1,2,3} #This is a set even though curly brackets are used
# print(type(set))

#======================================

# mixed data types (all immutable)

# set = {3.2, "hi", (1,2,3)}
# print(type(set))
# #TypeError: 'set' object is not subscriptable
# print(set[0])

#======================================
# no duplicates

# set = {3.2, "hi", (1,2,3)}
# print(set)

#======================================

# cannot have mutable (list) in a set
# set = {3.2, "hi", [1,2,3]}
#TypeError: unhashable type: 'list'
# print(set)

'''
Boolean Type (True or False)
'''

# print(type(True))

# boolean as numbers
# print(True == 1)
# print(False == 0)

# interesting logic
# print(True + True)

# not boolean operator
# print(not True)
# print(not False)

# and boolean operator
# print(True and False)
# print(True and True)
# print(False and False)

# or boolean operator
print(True or False)
print(True or True)
print(False or False)

