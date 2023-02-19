# function: - block of statement which can be used repetitively in program.

# creating a functions - defining
# calling a function
# arguments
# return type
# ! can not be called before created/defined

# creating
def func():
    print('hello from th simple functions')


# calling
func()  # hello from th simple functions

# -------------------------------------------------------
# arguments


# def fun1(arg1, arg2):
#     print('args', arg1, arg2)


# def sum(val1, val2):
#     print('sum:', val1+val2)


# fun1(1, 'yo')  # args 1 yo
# sum(10, 20)

# --------------------------------------------------------
# argument default value - when valuea re not passed at the time of calling , it can take default values - if args passed then they will override deafults
# def fun2(arg1=10, arg2=20):
#     print('args', arg1, arg2)


# fun2()  # args 10 20
# fun2(20)  # args 20 20

# --------------------------------------------------------
# using return
def fun3(arg=10):
    return arg*arg


x = fun3()
y = fun3(20)
print(x)  # 100
print(y)  # 400
