
'''
# BEFORE USING A DECORATOR
def some_function(number):
    print ("{}".format(number+1))
'''
"""
>>> some_function(11)
12
>>> some_function(8)
9
>>> some_function(1)
2
"""


# AFTER USING A DECORATOR
def history_decorator(my_function):
    history = []  # list

    def wrapper(my_argument):  # creates a function wrapper within a function
        history.append(my_argument)  # since defined in this scope,has snapshot
        my_function(my_argument)        # of history list.
        print ("History: {}".format(history))
    return wrapper  # returns a function wrapper from a function


# These 3 lines are equivalent to the bottom 3 lines
@history_decorator
def some_function(number):
    print ("{}".format(number + 1))


# These 3 lines are equivalent to the above 3 lines
def some_function(number):
    print ("{}".format(number + 1))


some_function = history_decorator(some_function)  # same as @history_decorator


some_function(11)   # testing
some_function(14)
"""
>>> some_function(11)
12
History: [11]
>>> some_function(8)
9
History: [11, 8]
>>> some_function(1)
2
History: [11, 8, 1]
"""


def addOne(myFunc):
    def addOneInside(*args, **kwargs):
        return myFunc(*args, **kwargs) + 1
    return addOneInside


@addOne
def oldFunc(x=0):
    return x


print ("{}".format(oldFunc()))  # testing
print ("{}".format(oldFunc(500)))
