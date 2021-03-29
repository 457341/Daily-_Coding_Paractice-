# Write a Python program to determine profiling of Python programs.

# Note: A profile is a set of statistics that describes how often and for how long 
# various parts of the program executed. These statistics can be formatted into reports via the pstats module.


import cProfile
def fun():
    print("This is fun()")

def print_name(name,surname,country):
    print("My name is: {}\nAnd my surname is: {}\nI from: {}".format(name,surname,country))


def sum_two_num(n1,n2):
    print("The addition of two number is: ",n1 + n2)
cProfile.run('fun()')
cProfile.run('print_name("Manzoor","Hussain","Pakistan")')
cProfile.run('sum_two_num(2,3)')