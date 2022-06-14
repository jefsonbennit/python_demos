import random
 
# Generates a random number between
# a given positive range
r1 = random.randint(0, 10)
print("Random number between 0 and 10 is % s" % (r1))

# Impure functions

# When a function 
# depends on variables or functions outside 
# of its definition block, you can never be 
# sure that the function will behave the same 
# every time it’s called. For example the 
# mathematical function random() will give 
# different outputs for the same function call.

# pure functions

# Pure functions are functions which 
# will give exact result when the same 
# arguments are passed

# subroutines

# Subroutines are small sections of code that are used to perform a particular task that 
# can be used repeatedly