

# arguments
# *args
# takes UNLIMITED regular arguments.
# place in function argument to use
# prevents program from crashing =P
def Func(*args):
    for arg in args:
        print (arg)


aList = [1, 2, 3, "ham"]
Func(1, 2, 3, "ham")
Func(aList)  # prints list as 1 item, or a whole
Func(*aList)  # separates a list of items.. also works with dictionary or tuple


# keyword arguments
# #kwargs
# same as args except declare the vars and amount within the function arguments
def Func(x=234, y=9):
    print(x, y)


Func()
Func(x=456, y=3)


def Func(**kwargs):  # interprets keyward arguments as tuples
    for item in kwargs.items():
        print(item)


Func(x=456, y=3)


def Func(*args, **kwargs):
    for arg in args:
        print (arg)
    for item in kwargs.items():
        print(item)


Func(1, 2, x=456, y=3)
